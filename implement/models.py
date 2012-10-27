from django.db import models
from django.forms import ModelForm


class Tillage(models.Model):
    TILLAGE_CHOICES = (
        ('Primary','Primary Tillage'),
        ('Secondary','Secondary Tillage'),
    )
    typeof = models.CharField("Type of tillage",max_length = 200, choices = TILLAGE_CHOICES)
    length = models.IntegerField("Length of Field")
    width = models.IntegerField("Width of Field")

    def __unicode__(self):
        return self.typeof

class TillageForm(ModelForm):
    class Meta:
        model = Tillage

class Tractor(models.Model):
	make = models.CharField("Make of Tractor",max_length = 200)
	model = models.CharField("Model number",max_length = 200)
	pto_power = models.IntegerField()
	rpm = models.IntegerField()
	max_torque = models.IntegerField()
	front_weight = models.IntegerField("Static weight on front tire")
	rear_weight = models.IntegerField("Static weight on rear tire")
	wheelbase = models.IntegerField()
	hitch_point = models.IntegerField("location of the hitch point")
	cg_rear = models.IntegerField("location of CG from the rear")
	cg_height = models.IntegerField("height of the CG")

	def __unicode__(self):
		return self.make


class TractorForm(ModelForm):
    class Meta:
        model = Tractor

class Tire(models.Model):
    TIRE_CHOICES = (
        ('bias', 'bias ply'),
        ('radial', 'radial ply'),
    )
    tire_type = models.CharField(max_length = 200, choices = TIRE_CHOICES)
    size = models.IntegerField()
    width = models.IntegerField()
    diameter = models.IntegerField()
    static_radius = models.IntegerField()
    capacity = models.IntegerField()
    ply_rating = models.IntegerField()
    tread_code = models.IntegerField()

    def __unicode__(self):
        return self.size

class TireForm(ModelForm):
    class Meta:
        model = Tire

class Implement(models.Model):
    IMPLEMENT_CHOICES = (
        ('moldboard','moldboard plough'),
        ('cultivator', 'cultivator'),
        ('harrow', 'Offset disk harrow'),
    )
    name = models.CharField(max_length = 200, choices = IMPLEMENT_CHOICES)
    size = models.IntegerField()
    number = models.IntegerField()
    bottom_width = models.IntegerField()
    implement_width = models.IntegerField()
    weight = models.IntegerField()
    cg_hitch = models.IntegerField("distance of CG of implement from hitch point of tractor")

    def __unicode__(self):
        return self.name

class ImplementForm(ModelForm):
    class Meta:
        model = Implement

class Other(models.Model):
    STRENGTH_CHOICES = (
        ('soft', 'soft soil'),
        ('firm', 'firm soil'),
        ('tilled', 'tilled soil'),
        ('hard', 'hard soil'),
    )
    TEXTURE_CHOICES = (
        ('Course', 'course soil'),
        ('Medium', 'medium soil'),
        ('Fine', 'fine soil'),
    )
    soil_texture = models.CharField(max_length = 200, choices = TEXTURE_CHOICES)
    soil_strength = models.CharField(max_length = 200, choices = STRENGTH_CHOICES)
    depth_tillage = models.IntegerField()
    speed = models.IntegerField()
    bulk_density = models.IntegerField()
    cone_index = models.IntegerField()

    def __unicode__(self):
        return self.soil_texture

class OtherForm(ModelForm):
    class Meta:
        model = Other

class Coefficient(models.Model):
    soil_texture_factor = models.IntegerField("Soil Texture Adjustment Factor")
    A = models.IntegerField("Soil and Machine Specific Factor(A)")
    B = models.IntegerField("Soil and Machine Specific Factor(B)")
    C = models.IntegerField("Soil and Machine Specific Factor(C)")
    A1 = models.IntegerField("Traction coefficient (A1)")
    A2 = models.IntegerField("Traction coefficient (A2)")
    A3 = models.IntegerField("Traction coefficient (A3)")
    A4 = models.IntegerField("Traction coefficient (A4)")
    A5 = models.IntegerField("Traction coefficient (A5)")
    A6 = models.IntegerField("Traction coefficient (A6)")
    A7 = models.IntegerField("Traction coefficient (A7)")
    a_2 = models.IntegerField("regression coefficient(a2)")
    b_2 = models.IntegerField("regression coefficient(b2)")
    c_2 = models.IntegerField("regression coefficient(c2)")


class CoefficientForm(ModelForm):
    class Meta:
        model = Coefficient 

