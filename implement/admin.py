from implement.models import Tractor
from django.contrib import admin

class TractorAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basic Information',{'fields':['make','model','pto_power']}),
		('Other Details',{'fields':['rpm','max_torque','front_weight','rear_weight','wheelbase','cg_rear','cg_height','hitch_point']}),
	]

admin.site.register(Tractor,TractorAdmin)
