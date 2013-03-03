#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from json_field import JSONField

from django.db import models
from django.template.defaultfilters import slugify

from rateflix.contexts import MovieContextManager
from rateflix.managers import MovieManager
from util.image import JPEGImageField

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^util\.image\.JPEGImageField"])

DEFAULT_FIELD_MAP = {
    'fields': ''
}

SCRAPER_CHOICES = (
    ('NetflixScraper', 'Netflix Scraper'),
)

# class WebPlatform(models.Model):
#     name = models.CharField(max_length=100)
#     url = models.CharField(max_length=255, blank=True)
#     auth_data = JSONField(null=True, blank=True)


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
    image = JPEGImageField(upload_to='image', null=True)
    release_year = models.CharField(null=True, max_length=15)
    country = models.CharField(null=True, max_length=200)
    rating = models.DecimalField(decimal_places=1, max_digits=4, default=0)
    tv_show = models.BooleanField(default=False)

    genre = models.ManyToManyField('rateflix.Genre', null=True)

    objects = MovieManager()

    def __unicode__(self):
        return '{}({})'.format(self.name, self.release_year)

    @property
    def genres(self):
        return '/'.join([genre.name for genre in self.genre.all()])

    @property
    def context_manager(self):
        return MovieContextManager(self)

# class MovieRating(models.Model):

#     movie = models.ForeignKey('rateflix.Movie', null=True)
#     platform = models.CharField(max_length=100, default='IMDB')
#     rating = models.DecimalField(decimal_places=1, max_digits=4, default=0)


class Genre(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __unicode__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)
