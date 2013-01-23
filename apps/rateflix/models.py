from json_field import JSONField

from django.db import models

from rateflix.managers import MovieManager

DEFAULT_FIELD_MAP = {
    'fields': ''
}

SCRAPER_CHOICES = (
    ('NetflixScraper', 'Netflix Scraper'),
)


class WatchPlatform(models.Model):

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)
    auth_data = JSONField(null=True, blank=True)
    scraper = models.CharField(choices=SCRAPER_CHOICES, max_length=63, null=True, blank=True)

    def __unicode__(self):
        return u'{}({})'.format(self.name, self.url)

    def get_scraper(self):
        if self.scraper:
            from rateflix import scrape as scrapers
            return getattr(scrapers, self.scraper)


class Movie(models.Model):

    name = models.CharField(max_length=1000)
    genre = models.ForeignKey('rateflix.Genre', null=True)
    # image = models.ImageField()
    release_year = models.PositiveSmallIntegerField(null=True)
    rating = models.DecimalField(decimal_places=1, max_digits=4, default=0)
    # watched = models.BooleanField(default=False)

    objects = MovieManager()


# class MovieRating(models.Model):

#     movie = models.ForeignKey('rateflix.Movie', null=True)
#     platform = models.CharField(max_length=100, default='IMDB')
#     rating = models.DecimalField(decimal_places=1, max_digits=4, default=0)


class Genre(models.Model):

    name = models.CharField(max_length=100)
