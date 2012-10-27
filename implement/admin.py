from implement.models import *
from django.contrib import admin

class TractorAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basic Information',{'fields':['make','model','pto_power']}),
		('Other Details',{'fields':['rpm','max_torque','front_weight','rear_weight','wheelbase','cg_rear','cg_height','hitch_point']}),
	]

admin.site.register(Tractor,TractorAdmin)
admin.site.register(Tire)
admin.site.register(Implement)
admin.site.register(Other)
admin.site.register(Coefficient)
