#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.loader import render_to_string

from util.thumborz import thumb


class ContextManager(object):
    pass


class MovieContextManager(ContextManager):

    def __init__(self, movie):
        self.movie = movie

    @property
    def pretty_name(self):
        return self.movie.name

    @property
    def pretty_imdb(self):
        return 'IMDB Rating: {}/10'.format(self.movie.rating)

    def get_json_context(self):
        return {
            'name': self.pretty_name,
            'imdb_rating': self.pretty_imdb,
            'image': thumb(self.movie.image),
            'description': render_to_string('contexts/movie_popover.html',
                        {'movie': self.movie})

        }
