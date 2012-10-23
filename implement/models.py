from django.db import models
from django.forms import ModelForm

class Tractor(models.Model):
	make = models.CharField(max_length = 200)
	model = models.CharField(max_length = 200)
	pto_power = models.IntegerField()
	rpm = models.IntegerField()
	max_torque = models.IntegerField()
	front_weight = models.IntegerField()
	rear_weight = models.IntegerField()
	wheelbase = models.IntegerField()
	hitch_point = models.IntegerField()
	cg_rear = models.IntegerField()
	cg_height = models.IntegerField()

	def __unicode__(self):
		return self.make


class TractorForm(ModelForm):
    class Meta:
        model = Tractor

class Tire(models.Model):
    types = models.CharField(max_length = 200)
    size = models.IntegerField()
    width = models.IntegerField()
    diameter = models.IntegerField()
    static_radius = models.IntegerField()
    capacity = models.IntegerField()
    rating = models.IntegerField()
    tread_code = models.IntegerField()

    def __unicode__(self):
        return self.size

class TireForm(ModelForm):
    class Meta:
        model = Tire
