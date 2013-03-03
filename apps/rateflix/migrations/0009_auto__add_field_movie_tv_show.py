# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.tv_show'
        db.add_column('rateflix_movie', 'tv_show',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Movie.tv_show'
        db.delete_column('rateflix_movie', 'tv_show')


    models = {
        'rateflix.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True', 'null': 'True'})
        },
        'rateflix.movie': {
            'Meta': {'object_name': 'Movie'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['rateflix.Genre']", 'null': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('util.image.JPEGImageField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '1'}),
            'release_year': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'tv_show': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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