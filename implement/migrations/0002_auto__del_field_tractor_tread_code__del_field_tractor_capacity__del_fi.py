# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Tractor.tread_code'
        db.delete_column('implement_tractor', 'tread_code')

        # Deleting field 'Tractor.capacity'
        db.delete_column('implement_tractor', 'capacity')

        # Deleting field 'Tractor.static_radius'
        db.delete_column('implement_tractor', 'static_radius')

        # Deleting field 'Tractor.ply_rating'
        db.delete_column('implement_tractor', 'ply_rating')

        # Adding field 'Tractor.static_radius_rear'
        db.add_column('implement_tractor', 'static_radius_rear',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Tractor.static_radius_front'
        db.add_column('implement_tractor', 'static_radius_front',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Tractor.capacity_front'
        db.add_column('implement_tractor', 'capacity_front',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Tractor.capacity_rear'
        db.add_column('implement_tractor', 'capacity_rear',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Tractor.ply_rating_front'
        db.add_column('implement_tractor', 'ply_rating_front',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Tractor.ply_rating_rear'
        db.add_column('implement_tractor', 'ply_rating_rear',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Tractor.tread_code_front'
        db.add_column('implement_tractor', 'tread_code_front',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=200),
                      keep_default=False)

        # Adding field 'Tractor.tread_code_rear'
        db.add_column('implement_tractor', 'tread_code_rear',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=200),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Tractor.tread_code'
        raise RuntimeError("Cannot reverse this migration. 'Tractor.tread_code' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Tractor.capacity'
        raise RuntimeError("Cannot reverse this migration. 'Tractor.capacity' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Tractor.static_radius'
        raise RuntimeError("Cannot reverse this migration. 'Tractor.static_radius' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Tractor.ply_rating'
        raise RuntimeError("Cannot reverse this migration. 'Tractor.ply_rating' and its values cannot be restored.")
        # Deleting field 'Tractor.static_radius_rear'
        db.delete_column('implement_tractor', 'static_radius_rear')

        # Deleting field 'Tractor.static_radius_front'
        db.delete_column('implement_tractor', 'static_radius_front')

        # Deleting field 'Tractor.capacity_front'
        db.delete_column('implement_tractor', 'capacity_front')

        # Deleting field 'Tractor.capacity_rear'
        db.delete_column('implement_tractor', 'capacity_rear')

        # Deleting field 'Tractor.ply_rating_front'
        db.delete_column('implement_tractor', 'ply_rating_front')

        # Deleting field 'Tractor.ply_rating_rear'
        db.delete_column('implement_tractor', 'ply_rating_rear')

        # Deleting field 'Tractor.tread_code_front'
        db.delete_column('implement_tractor', 'tread_code_front')

        # Deleting field 'Tractor.tread_code_rear'
        db.delete_column('implement_tractor', 'tread_code_rear')


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
            'capacity_front': ('django.db.models.fields.FloatField', [], {}),
            'capacity_rear': ('django.db.models.fields.FloatField', [], {}),
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
            'ply_rating_front': ('django.db.models.fields.FloatField', [], {}),
            'ply_rating_rear': ('django.db.models.fields.FloatField', [], {}),
            'pto_power': ('django.db.models.fields.FloatField', [], {}),
            'rear_weight': ('django.db.models.fields.FloatField', [], {}),
            'rpm': ('django.db.models.fields.FloatField', [], {}),
            'rpm_torque': ('django.db.models.fields.FloatField', [], {}),
            'section_width_front': ('django.db.models.fields.FloatField', [], {}),
            'section_width_rear': ('django.db.models.fields.FloatField', [], {}),
            'static_radius_front': ('django.db.models.fields.FloatField', [], {}),
            'static_radius_rear': ('django.db.models.fields.FloatField', [], {}),
            'tire_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tread_code_front': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tread_code_rear': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wheelbase': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['implement']