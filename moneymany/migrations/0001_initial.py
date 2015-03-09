# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comdecide'
        db.create_table(u'moneymany_comdecide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('paytime', self.gf('django.db.models.fields.IntegerField')()),
            ('happytime', self.gf('django.db.models.fields.IntegerField')()),
            ('image_urls', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'moneymany', ['Comdecide'])


    def backwards(self, orm):
        # Deleting model 'Comdecide'
        db.delete_table(u'moneymany_comdecide')


    models = {
        u'moneymany.comdecide': {
            'Meta': {'object_name': 'Comdecide'},
            'happytime': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_urls': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'paytime': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['moneymany']