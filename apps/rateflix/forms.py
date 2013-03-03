#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from rateflix.models import Movie, Genre
from util.image import ImageProcessor


class ModelMultipleChoiceGetOrCreate(forms.ModelMultipleChoiceField):

    def clean(self, value):
        if isinstance(value, basestring):
            value = value.split(',')
        if not value:
            return []
        return [self.queryset.model.objects.get_or_create(name=name)[0] for name in value]


class MovieForm(forms.ModelForm):

    genre = ModelMultipleChoiceGetOrCreate(queryset=Genre.objects)

    class Meta:
        model = Movie
        fields = ('rating',
                  'release_year',
                  'genre',
                  'tv_show',
                  'country'
                )

    def clean_country(self):
        country = self.cleaned_data.get('country')
        return country

    def save(self, *args, **kwargs):
        image_file = ImageProcessor.process('image', self.data['image'])
        self.instance.image.save('image_name', image_file, save=False)
        super(MovieForm, self).save(*args, **kwargs)
