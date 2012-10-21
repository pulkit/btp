from implement.models import Tractor 
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def create(request):
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
		return HttpResponseRedirect("Thank you")
	else:
		return render_to_response("tractor.html",context_instance = RequestContext(request))



