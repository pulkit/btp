from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.formtools.wizard.views import SessionWizardView

from implement.models import Tractor 
"""def create(request):
	error_msg = u"NO POST data sent."
	if request.method == "POST":
		post = request.POST.copy()
		model = post['model']
		make = post['make']
		power = post['power']
		rpm = post['rpm']
		torque = post['torque']
		front_weight = post['front_weight']
		rear_weight = post['rear_weight']
		wheelbase = post['wheelbase']
		hitch_point = post['hitch_point']
		cg_rear = post['cg_rear']
		cg_height = post['cg_height']
		Tractor.objects.create(model = model,make = make,pto_power = power , rpm = rpm , max_torque = torque , front_weight = front_weight , rear_weight = rear_weight , wheelbase =wheelbase,hitch_point = hitch_point , cg_rear = cg_rear , cg_height = cg_height)
		return HttpResponse(u"Thank you")
	else:
		return render_to_response("tractor.html",context_instance = RequestContext(request))"""


class DSSWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        for form in form_list:
            form.save()
        return HttpResponseRedirect("thank you")    
