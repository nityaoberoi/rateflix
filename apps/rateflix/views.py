#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.views.generic.base import TemplateView, View
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

from rateflix.models import Movie, Genre


class LandingView(TemplateView):

    template_name = 'movies.html'

    def get(self, request, *args, **kwargs):
        genre = request.GET.get('genre')
        if genre:
            kwargs['genre__name'] = genre
        context = self.get_context_data(**kwargs)
        if request.is_ajax():
            import ipdb; ipdb.set_trace();
            return HttpResponse(json.dumps(context, cls=DjangoJSONEncoder),
                            mimetype='application/json')
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        data = {
            # 'genres': Genre.objects.exclude(movie=None).order_by('name'),
            'movies': self.get_movies(**kwargs),
            'types': ['TV show', 'movie', 'anything']
        }
        return data

    def get_movies(self, **filters):
        movies = (Movie
                .objects
                .filter(**filters)
                .rated()
                .order_by('-rating')[:10])
        return [movie.context_manager.get_json_context()
                    for movie in movies]


class AutocompleteView(View):

    def get(self, request, *args, **kwargs):
        self.query = request.GET.get('search')
        payload = self.get_context_data()
        return HttpResponse(json.dumps(payload, cls=DjangoJSONEncoder),
                    mimetype='application/json')

    def get_context_data(self, **kwargs):
        genres = list(Genre
                    .objects
                    .filter(name__icontains=self.query)
                    .values_list('name', flat=True))
        return [[index, genre, genre] for index, genre in enumerate(genres)]
