from django.db import models
from django.forms import ModelForm
from django import forms

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
TILLAGE_CHOICES = (
    ('Primary','Primary Tillage'),
    ('Secondary','Secondary Tillage'),
)
TIRE_CHOICES = (
    ('bias', 'bias ply'),
    ('radial', 'radial ply'),
    ('pneumatic','pneumatic ribbed'),
)
IMPLEMENT_CHOICES = (
    ('moldboard','moldboard plough'),
    ('cultivator', 'cultivator'),
    ('harrow', 'Offset disk harrow'),
)
 
 
class Tillage(models.Model):
    typeof = models.CharField("Type of tillage",max_length = 200, choices = TILLAGE_CHOICES)
    length = models.FloatField("Length of Field")
    width = models.FloatField("Width of Field")

    def __unicode__(self):
        return self.typeof

class TillageForm(ModelForm):
    class Meta:
        model = Tillage
                  
class Tractor(models.Model):
    make = models.CharField("Make of Tractor",max_length = 200) 
    model = models.CharField("Model number",max_length = 200,)
    pto_power = models.FloatField()
    rpm = models.FloatField("Rated Engine RPM at PTO Power ")
    rpm_torque = models.FloatField("Rated Engine RPM at maximum torque ")
    max_torque = models.FloatField("Maximum Engine Torue (in Nm )")
    front_weight = models.FloatField("Static weight on front tire ( in N )")
    rear_weight = models.FloatField("Static weight on rear tire( in N )",)
    wheelbase = models.FloatField()
    hitch_point = models.FloatField("location of the hitch point ( in m )",)
    cg_rear = models.FloatField("location of CG from the rear ( in m )",)
    cg_height = models.FloatField("height of the CG ( in m )",)
    tire_type = models.CharField(max_length = 200, choices = TIRE_CHOICES)
    section_width_front = models.FloatField(" Section Width of front tire ( in m )")
    section_width_rear =  models.FloatField(" Section width of rear tire ( in m )" )
    overall_diameter_rear =  models.FloatField(" Overall diameter of rear ( in m )")
    overall_diameter_front = models.FloatField(" Overall diameter of front ( in m )")
    static_radius_rear = models.FloatField("Static Loaded Radius of rear tire")
    static_radius_front = models.FloatField("Static Loaded Radius of front tire")
    capacity_front = models.FloatField(" Rated Capacity of front tire(in KN )")
    capacity_rear = models.FloatField(" Rated Capacity of rear tire (in KN )")
    ply_rating_front = models.FloatField(" Ply Rating of front tire")
    ply_rating_rear = models.FloatField("Ply Rating of rear tire")
    tread_code_front = models.CharField(" Tread Code of front tire",max_length = 200)
    tread_code_rear = models.CharField(" Tread Code of rear tire",max_length = 200)

    def __unicode__(self):
        return self.model

class BasicTractorForm(ModelForm):
    
    make = forms.ChoiceField(choices = tuple((t.make,t.make) for t in  Tractor.objects.all()))
    model =forms.ChoiceField(choices = tuple((t.model,t.model) for t in  Tractor.objects.all()))       
    class  Meta:
        model = Tractor
        fields = ('make','model',)

class AdvancedTractorForm(ModelForm):
    class Meta:
        model = Tractor
        fields = ('pto_power','rpm','rpm_torque','max_torque','front_weight','rear_weight','wheelbase','hitch_point','cg_rear','cg_height',)

class TireForm(ModelForm):
    class Meta:
        model = Tractor
        fields = ('tire_type','section_width_front','section_width_rear','overall_diameter_front','overall_diameter_rear','static_radius_rear','static_radius_front','capacity_front','capacity_rear','ply_rating_front','ply_rating_rear','tread_code_front','tread_code_rear')

class Implement(models.Model):
    name = models.CharField(max_length = 200, choices = IMPLEMENT_CHOICES)
    number = models.IntegerField(" No. of Bottoms")
    bottom_width = models.FloatField(" Bottom Width ( in cm )")
    implement_width = models.FloatField(" Implement Width ( in m )")
    weight = models.FloatField(" Weight of Implement ( in N )")
    cg_hitch = models.FloatField("distance of CG of implement from hitch point of tractor ( in m )")

    def __unicode__(self):
        return self.name

class ImplementForm(ModelForm):
    class Meta:
        model = Implement

class Soil(models.Model):
    soil_texture = models.CharField(max_length = 200, choices = TEXTURE_CHOICES)
    soil_strength = models.CharField(max_length = 200, choices = STRENGTH_CHOICES)
    bulk_density = models.FloatField(" Bulk Density ( in g/cc)")
    cone_index = models.FloatField("Cone Index ( in Kpa )")

    def __unicode__(self):
        return self.soil_texture

class SoilForm(ModelForm):
    class Meta:
        model = Soil
        

class Other(models.Model):
    depth_tillage = models.FloatField(" Depth of Operation( in cm )")
    speed = models.FloatField(" Speed of Operation ( in Km/h )")

    def __unicode__(self):
        return str(self.speed)
    

class OtherForm(ModelForm):
    class Meta:
        model = Other

class TireCoefficients(models.Model):
    tire_type = models.CharField(max_length = 200, choices = TIRE_CHOICES)
    A1 = models.FloatField("Traction coefficient (A1)")
    A2 = models.FloatField("Traction coefficient (A2)")
    A3 = models.FloatField("Traction coefficient (A3)")
    A4 = models.FloatField("Traction coefficient (A4)")
    A5 = models.FloatField("Traction coefficient (A5)")
    A6 = models.FloatField("Traction coefficient (A6)")
    A7 = models.FloatField("Traction coefficient (A7)")
    A8 = models.FloatField("Traction coefficient (A8)")
    def __unicode__(self):
        return str(self.tire_type)

class TireCoefficientsForm(ModelForm):
    class Meta:
        model = TireCoefficients



class SoilCoefficients(models.Model):
    soil_texture = models.CharField(max_length = 200, choices = TEXTURE_CHOICES) 
    A = models.FloatField("Soil and Machine Specific Factor(A)")
    B = models.FloatField("Soil and Machine Specific Factor(B)")
    C = models.FloatField("Soil and Machine Specific Factor(C)")
    soil_texture_factor = models.FloatField("Soil Texture Adjustment Factor")

    def __unicode__(self):
        return self.soil_texture

class SoilCoefficientsForm(ModelForm):
    class Meta:
        model = SoilCoefficients
    


