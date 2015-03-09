# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'moneymany_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
        ))
        db.send_create_signal(u'moneymany', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'moneymany_message')


    models = {
        u'moneymany.computer': {
            'Meta': {'object_name': 'Computer'},
            'happytime': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_urls': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'paytime': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'moneymany.message': {
            'Meta': {'object_name': 'Message'},
            'createtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['moneymany']