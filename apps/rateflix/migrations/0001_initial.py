# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WatchPlatform'
        db.create_table('rateflix_watchplatform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('auth_data', self.gf('json_field.fields.JSONField')(default='null', null=True, blank=True)),
            ('scraper', self.gf('django.db.models.fields.CharField')(max_length=63, null=True, blank=True)),
        ))
        db.send_create_signal('rateflix', ['WatchPlatform'])

        # Adding model 'Movie'
        db.create_table('rateflix_movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rateflix.Genre'], null=True)),
            ('release_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
        ))
        db.send_create_signal('rateflix', ['Movie'])

        # Adding model 'MovieRating'
        db.create_table('rateflix_movierating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rateflix.Movie'], null=True)),
            ('platform', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rateflix.WatchPlatform'], null=True)),
            ('rating', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=1)),
        ))
        db.send_create_signal('rateflix', ['MovieRating'])

        # Adding model 'Genre'
        db.create_table('rateflix_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('rateflix', ['Genre'])


    def backwards(self, orm):
        # Deleting model 'WatchPlatform'
        db.delete_table('rateflix_watchplatform')

        # Deleting model 'Movie'
        db.delete_table('rateflix_movie')

        # Deleting model 'MovieRating'
        db.delete_table('rateflix_movierating')

        # Deleting model 'Genre'
        db.delete_table('rateflix_genre')


    models = {
        'rateflix.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rateflix.movie': {
            'Meta': {'object_name': 'Movie'},
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rateflix.Genre']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
        },
        'rateflix.movierating': {
            'Meta': {'object_name': 'MovieRating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rateflix.Movie']", 'null': 'True'}),
            'platform': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rateflix.WatchPlatform']", 'null': 'True'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '1'})
        },
        'rateflix.watchplatform': {
            'Meta': {'object_name': 'WatchPlatform'},
            'auth_data': ('json_field.fields.JSONField', [], {'default': "'null'", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'scraper': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['rateflix']