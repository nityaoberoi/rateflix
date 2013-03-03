import copy
from pyquery import PyQuery as pq
import requests
import urllib

from rateflix.forms import MovieForm
from rateflix.models import Movie


class Scraper(object):

    def __init__(self, auth_data=None, **kwargs):
        self.auth_data = copy.copy(auth_data) or {}
        self.session = requests.session()

    def get_document(self, url):
        response = self.get_response(url)
        return pq(response.text)

    def get_response(self, url):
        if self.auth_data and not self.authenticated:
            self.authenticate(url)
        return self.session.get(url)

    @property
    def authenticated(self):
        return self.session.cookies.items()

    def authenticate(self, url):
        request_url = self.auth_data.pop('auth_url', url)
        self.session.post(
            request_url,
            data=self.auth_data)

    def get_item(self, doc, path, key=None):
        paths = path.split('||')
        for path in paths:
            value = doc(path)
            if value:
                break
        ret_values = map(lambda item: item.text.strip(), value)
        if ret_values and len(ret_values) == 1:
            return ret_values[0]
        return ret_values or None


class NetflixScraper(Scraper):

    def authenticate(self, url):
        request_url = self.auth_data.get('auth_url', url)
        response = self.session.get(request_url)
        doc = pq(response.text)
        self.auth_data.update({
            "authURL": self.get_item(doc, 'input[name="authURL"]').value
        })
        super(NetflixScraper, self).authenticate(url)

    def process(self, url):
        doc = self.get_document(url)
        self.scrape_movies(doc)

    def scrape_movies(self, doc):
        movie_xpath = '.boxShotImg'
        map(lambda movie: self.add_movie(movie.get('alt')),
                        doc(movie_xpath))

    def add_movie(self, name):
        Movie.objects.get_or_create(name=name)


IMDB_DICT = {
    "rating": ".titlePageSprite.star-box-giga-star",
    "release_year": ".header span a || .header span.nobr",
    "image": "td#img_primary div.image img",
    "genre": ".infobar a[href*=genre]",
    "tv_show": ".infobar",
    "country": ".infobar .nobr a",
}

IMAGE_FIELDS = ['image']


class IMDBScraper(Scraper):

    BASE_URL = "http://www.imdb.com"
    SEARCH_URL = 'http://www.imdb.com/find?q={}'

    def process(self, url, movie):
        if not url.startswith('http'):
            url = '{}{}'.format(self.BASE_URL, url)
        doc = self.get_document(url)
        self.add_rating(doc, movie)

    def get_movie_url(self, movie_name):
        result_xpath = ".findResult .result_text a"
        search_url = self.SEARCH_URL.format(urllib.quote_plus(movie_name))
        doc = self.get_document(search_url)
        # route the url to the first search result
        value = None
        try:
            value = doc(result_xpath).eq(0)[0].get('href')
        except IndexError:
            pass
        return value

    def get_item(self, doc, path, key):
        if key in IMAGE_FIELDS:
            return doc(path).attr('src')
        return super(IMDBScraper, self).get_item(doc, path)

    def add_rating(self, doc, movie):
        data = {}
        for key in IMDB_DICT.keys():
            value = self.get_item(doc, IMDB_DICT.get(key), key)
            data[key] = value
        form = MovieForm(data=data, instance=movie)
        if form.is_valid():
            form.save()
