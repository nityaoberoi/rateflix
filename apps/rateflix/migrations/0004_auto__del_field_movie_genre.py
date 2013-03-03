# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Movie.genre'
        db.delete_column('rateflix_movie', 'genre_id')

        # Adding M2M table for field genre on 'Movie'
        db.create_table('rateflix_movie_genre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm['rateflix.movie'], null=False)),
            ('genre', models.ForeignKey(orm['rateflix.genre'], null=False))
        ))
        db.create_unique('rateflix_movie_genre', ['movie_id', 'genre_id'])


    def backwards(self, orm):
        # Adding field 'Movie.genre'
        db.add_column('rateflix_movie', 'genre',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rateflix.Genre'], null=True),
                      keep_default=False)

        # Removing M2M table for field genre on 'Movie'
        db.delete_table('rateflix_movie_genre')


    models = {
        'rateflix.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rateflix.movie': {
            'Meta': {'object_name': 'Movie'},
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['rateflix.Genre']", 'null': 'True', 'symmetrical': 'False'}),
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