# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tillage'
        db.create_table('implement_tillage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('typeof', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('width', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('implement', ['Tillage'])

        # Adding model 'Tractor'
        db.create_table('implement_tractor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pto_power', self.gf('django.db.models.fields.FloatField')()),
            ('rpm', self.gf('django.db.models.fields.FloatField')()),
            ('rpm_torque', self.gf('django.db.models.fields.FloatField')()),
            ('max_torque', self.gf('django.db.models.fields.FloatField')()),
            ('front_weight', self.gf('django.db.models.fields.FloatField')()),
            ('rear_weight', self.gf('django.db.models.fields.FloatField')()),
            ('wheelbase', self.gf('django.db.models.fields.FloatField')()),
            ('hitch_point', self.gf('django.db.models.fields.FloatField')()),
            ('cg_rear', self.gf('django.db.models.fields.FloatField')()),
            ('cg_height', self.gf('django.db.models.fields.FloatField')()),
            ('tire_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('section_width_front', self.gf('django.db.models.fields.FloatField')()),
            ('section_width_rear', self.gf('django.db.models.fields.FloatField')()),
            ('overall_diameter_rear', self.gf('django.db.models.fields.FloatField')()),
            ('overall_diameter_front', self.gf('django.db.models.fields.FloatField')()),
            ('static_radius', self.gf('django.db.models.fields.FloatField')()),
            ('capacity', self.gf('django.db.models.fields.FloatField')()),
            ('ply_rating', self.gf('django.db.models.fields.FloatField')()),
            ('tread_code', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('implement', ['Tractor'])

        # Adding model 'Implement'
        db.create_table('implement_implement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('bottom_width', self.gf('django.db.models.fields.FloatField')()),
            ('implement_width', self.gf('django.db.models.fields.FloatField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('cg_hitch', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('implement', ['Implement'])

        # Adding model 'Soil'
        db.create_table('implement_soil', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('soil_texture', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('soil_strength', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bulk_density', self.gf('django.db.models.fields.FloatField')()),
            ('cone_index', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('implement', ['Soil'])

        # Adding model 'Other'
        db.create_table('implement_other', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('depth_tillage', self.gf('django.db.models.fields.FloatField')()),
            ('speed', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('implement', ['Other'])

        # Adding model 'TireCoefficients'
        db.create_table('implement_tirecoefficients', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tire_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('A1', self.gf('django.db.models.fields.FloatField')()),
            ('A2', self.gf('django.db.models.fields.FloatField')()),
            ('A3', self.gf('django.db.models.fields.FloatField')()),
            ('A4', self.gf('django.db.models.fields.FloatField')()),
            ('A5', self.gf('django.db.models.fields.FloatField')()),
            ('A6', self.gf('django.db.models.fields.FloatField')()),
            ('A7', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('implement', ['TireCoefficients'])

        # Adding model 'SoilCoefficients'
        db.create_table('implement_soilcoefficients', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('soil_texture', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('A', self.gf('django.db.models.fields.FloatField')()),
            ('B', self.gf('django.db.models.fields.FloatField')()),
            ('C', self.gf('django.db.models.fields.FloatField')()),
            ('soil_texture_factor', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('implement', ['SoilCoefficients'])


    def backwards(self, orm):
        # Deleting model 'Tillage'
        db.delete_table('implement_tillage')

        # Deleting model 'Tractor'
        db.delete_table('implement_tractor')

        # Deleting model 'Implement'
        db.delete_table('implement_implement')

        # Deleting model 'Soil'
        db.delete_table('implement_soil')

        # Deleting model 'Other'
        db.delete_table('implement_other')

        # Deleting model 'TireCoefficients'
        db.delete_table('implement_tirecoefficients')

        # Deleting model 'SoilCoefficients'
        db.delete_table('implement_soilcoefficients')


    models = {
        'implement.implement': {
            'Meta': {'object_name': 'Implement'},
            'bottom_width': ('django.db.models.fields.FloatField', [], {}),
            'cg_hitch': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implement_width': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        'implement.other': {
            'Meta': {'object_name': 'Other'},
            'depth_tillage': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speed': ('django.db.models.fields.FloatField', [], {})
        },
        'implement.soil': {
            'Meta': {'object_name': 'Soil'},
            'bulk_density': ('django.db.models.fields.FloatField', [], {}),
            'cone_index': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'soil_strength': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'soil_texture': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'implement.soilcoefficients': {
            'A': ('django.db.models.fields.FloatField', [], {}),
            'B': ('django.db.models.fields.FloatField', [], {}),
            'C': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'object_name': 'SoilCoefficients'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'soil_texture': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'soil_texture_factor': ('django.db.models.fields.FloatField', [], {})
        },
        'implement.tillage': {
            'Meta': {'object_name': 'Tillage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'typeof': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'width': ('django.db.models.fields.FloatField', [], {})
        },
        'implement.tirecoefficients': {
            'A1': ('django.db.models.fields.FloatField', [], {}),
            'A2': ('django.db.models.fields.FloatField', [], {}),
            'A3': ('django.db.models.fields.FloatField', [], {}),
            'A4': ('django.db.models.fields.FloatField', [], {}),
            'A5': ('django.db.models.fields.FloatField', [], {}),
            'A6': ('django.db.models.fields.FloatField', [], {}),
            'A7': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'object_name': 'TireCoefficients'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tire_type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'implement.tractor': {
            'Meta': {'object_name': 'Tractor'},
            'capacity': ('django.db.models.fields.FloatField', [], {}),
            'cg_height': ('django.db.models.fields.FloatField', [], {}),
            'cg_rear': ('django.db.models.fields.FloatField', [], {}),
            'front_weight': ('django.db.models.fields.FloatField', [], {}),
            'hitch_point': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'max_torque': ('django.db.models.fields.FloatField', [], {}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'overall_diameter_front': ('django.db.models.fields.FloatField', [], {}),
            'overall_diameter_rear': ('django.db.models.fields.FloatField', [], {}),
            'ply_rating': ('django.db.models.fields.FloatField', [], {}),
            'pto_power': ('django.db.models.fields.FloatField', [], {}),
            'rear_weight': ('django.db.models.fields.FloatField', [], {}),
            'rpm': ('django.db.models.fields.FloatField', [], {}),
            'rpm_torque': ('django.db.models.fields.FloatField', [], {}),
            'section_width_front': ('django.db.models.fields.FloatField', [], {}),
            'section_width_rear': ('django.db.models.fields.FloatField', [], {}),
            'static_radius': ('django.db.models.fields.FloatField', [], {}),
            'tire_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tread_code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wheelbase': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['implement']