from django.core.management.base import BaseCommand

from rateflix.models import WatchPlatform


class Command(BaseCommand):
    """
    Entry point for getting movies from all platforms
    """

    def handle(self, *args, **options):

        for platform in WatchPlatform.objects.all():
            Scraper = platform.get_scraper()
            scraper = Scraper(platform.auth_data)
            scraper.process(platform.url)
