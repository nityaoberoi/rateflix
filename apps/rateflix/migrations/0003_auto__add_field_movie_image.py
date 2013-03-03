# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.image'
        db.add_column('rateflix_movie', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Movie.image'
        db.delete_column('rateflix_movie', 'image')


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '1'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
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