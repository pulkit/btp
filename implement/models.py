from django.db import models

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

# Create your models here.
