from django.core.management.base import BaseCommand

from rateflix.models import Movie
from rateflix.scrape import IMDBScraper


class Command(BaseCommand):
    """
    Entry point for getting movies from all platforms
    """

    def handle(self, *args, **options):
        imdb_scraper = IMDBScraper()
        for movie in Movie.objects.all().unrated():
            movie_url = imdb_scraper.get_movie_url(movie.name.rsplit('(')[0])
            if movie_url:
                try:
                    imdb_scraper.process(movie_url, movie)
                except Exception as e:
                    pass
