from models import *
from django.contrib import admin

class TractorAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basic Information',{'fields':['make','model','pto_power']}),
		('Other Details',{'fields':['rpm','max_torque','rpm_torque','front_weight','rear_weight','wheelbase','cg_rear','cg_height','hitch_point']}),
		('Tire Details',{'fields':['tire_type','section_width_front','section_width_rear','overall_diameter_rear','overall_diameter_front','static_radius_rear','static_radius_front','capacity_front','capacity_rear','ply_rating_rear','ply_rating_front','tread_code_front','tread_code_rear']}),
	
	]

admin.site.register(Tractor,TractorAdmin)
admin.site.register(Implement)
admin.site.register(Other)
admin.site.register(TireCoefficients)
admin.site.register(SoilCoefficients)
admin.site.register(Soil)
