from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.formtools.wizard.views import SessionWizardView
from django.contrib.formtools.wizard.views import WizardView

from implement.models import Tractor 

class DSSWizard(SessionWizardView):
    def get_template_names(self):
        return ['form.html'.format(self.steps.current)] 
           
    def done(self, form_list, **kwargs):
        tractor = form_list[0].save()
        tire = form_list[1].save()
        implement = form_list[2].save()
        other = form_list[3].save()
        coefficient = form_list[4].save()
        P = tractor.pto_power
        rpm = tractor.rpm
        T = tractor.max_torque
        FW = tractor.front_weight
        RW = tractor.rear_weight
        WB = tractor.wheelbase
        HP = tractor.hitch_point
        cg_rear = tractor.cg_rear
        cg_height = tractor.cg_height
        tire_size = tire.tire_size
        tire_width = tire.tire_width
        dia = tire.diameter
        SR = tire.static_radius
        cap = tire.capacity
        PR = tire.ply_rating
        TC = tire.tread_code
        imp_size = implement.size
        n = implement.number
        BW = implement.bottom_width
        IW = implement.implement_width
        w = implement.weight
        CH = implement.cg_hitch
        TD = other.tillage_depth
        v = other.speed
        BD = other.bulk_density
        ci = other.cone_index
        f = coefficient.soil_texture_factor
        a = coefficient.A
        b = coefficient.B
        c = coefficient.C
        a1 = coefficient.A1
        a2 = coefficient.A2
        a3 = coefficient.A3
        a4 = coefficient.A4
        a5 = coefficient.A5
        a6 = coefficient.A6
        a7 = coefficient.A7
        a_2 = coefficient.a_2
        b_2 = coefficient.b_2
        c_2 = coefficient.c_2

        return HttpResponse(m0.make)
    
   
