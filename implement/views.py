from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.formtools.wizard.views import SessionWizardView
from models import *
from django.shortcuts import render_to_response

from math import*

from kookoo_sms import send_kookoo_sms

class DSSWizard(SessionWizardView):
    def get_template_names(self):
        return ['form.html'.format(self.steps.current)] 
     
    def get_form_initial(self,step): 
        if step == '1':
           data = self.storage.get_step_data('0')
           tractor = Tractor.objects.filter(make = data['0-make'],model = data['0-model'])[:1]
           return self.initial_dict.get(step, {'pto_power':tractor[0].pto_power,'rpm_torque':tractor[0].rpm_torque,'rpm':tractor[0].rpm,'max_torque':tractor[0].max_torque,'front_weight':tractor[0].front_weight,'rear_weight':tractor[0].rear_weight,'wheelbase':tractor[0].wheelbase,'hitch_point':tractor[0].hitch_point,'cg_rear':tractor[0].cg_rear,'cg_height':tractor[0].cg_height,'tire_type':tractor[0].tire_type,'section_width_front':tractor[0].section_width_front,'section_width_rear':tractor[0].section_width_rear,'overall_diameter_rear':tractor[0].overall_diameter_rear,'overall_diameter_front':tractor[0].overall_diameter_front,'static_radius_rear':tractor[0].static_radius_rear,'static_radius_front':tractor[0].static_radius_front,'capacity_front':tractor[0].capacity_front,'capacity_rear':tractor[0].capacity_rear,'ply_rating_front':tractor[0].ply_rating_front,'ply_rating_rear':tractor[0].ply_rating_rear,'tread_code_front':tractor[0].tread_code_front,'tread_code_rear':tractor[0].tread_code_rear,})     
        if step == '2':
            data = self.storage.get_step_data('0')
            tractor = Tractor.objects.filter(make = data['0-make'],model = data['0-model'])[:1]
            return self.initial_dict.get(step, {'pto_power':tractor[0].pto_power,'rpm_torque':tractor[0].rpm_torque,'rpm':tractor[0].rpm,'max_torque':tractor[0].max_torque,'front_weight':tractor[0].front_weight,'rear_weight':tractor[0].rear_weight,'wheelbase':tractor[0].wheelbase,'hitch_point':tractor[0].hitch_point,'cg_rear':tractor[0].cg_rear,'cg_height':tractor[0].cg_height,'tire_type':tractor[0].tire_type,'section_width_front':tractor[0].section_width_front,'section_width_rear':tractor[0].section_width_rear,'overall_diameter_rear':tractor[0].overall_diameter_rear,'overall_diameter_front':tractor[0].overall_diameter_front,'static_radius_rear':tractor[0].static_radius_rear,'static_radius_front':tractor[0].static_radius_front,'capacity_front':tractor[0].capacity_front,'capacity_rear':tractor[0].capacity_rear,'ply_rating_front':tractor[0].ply_rating_front,'ply_rating_rear':tractor[0].ply_rating_rear,'tread_code_front':tractor[0].tread_code_front,'tread_code_rear':tractor[0].tread_code_rear,})     
        if step == '5':
            data = self.storage.get_step_data('0')
            tractor = Tractor.objects.filter(make = data['0-make'],model = data['0-model'])[:1]
            tractor_coefficients = TireCoefficients.objects.filter(tire_type = tractor[0].tire_type)[:1]
            return self.initial_dict.get(step, {'tire_type':tractor_coefficients[0].tire_type,'A1':tractor_coefficients[0].A1,'A2':tractor_coefficients[0].A2,'A3':tractor_coefficients[0].A3,'A4':tractor_coefficients[0].A4,'A5':tractor_coefficients[0].A5,'A6':tractor_coefficients[0].A6,'A7':tractor_coefficients[0].A7,'A8':tractor_coefficients[0].A8,})     
        if step == '7':
            data = self.storage.get_step_data('6')          
            soil_coefficients = SoilCoefficients.objects.filter(soil_texture = data['6-soil_texture'])[:1]
            print soil_coefficients
            return self.initial_dict.get(step, {'soil_texture':soil_coefficients[0].soil_texture,'A':soil_coefficients[0].A,'B':soil_coefficients[0].B,'C':soil_coefficients[0].C,'soil_texture_factor':soil_coefficients[0].soil_texture_factor})     
 
               
    def done(self, form_list, **kwargs):
        tractor1 = form_list[0].save(commit = False)     
        tractor2 = form_list[1].save(commit= False)
        tractor3 = form_list[2].save(commit= False)
        tractor3.model = tractor1.model
        tractor3.make = tractor1.make
        tractor3.pto_power = tractor2.pto_power
        tractor3.rpm = tractor2.rpm
        tractor3.rpm_torque = tractor2.rpm_torque
        tractor3.max_torque = tractor2.max_torque
        tractor3.front_weight = tractor2.front_weight
        tractor3.rear_weight = tractor2.rear_weight
        tractor3.wheelbase = tractor2.wheelbase
        tractor3.hitch_point = tractor2.hitch_point
        tractor3.cg_rear = tractor2.cg_rear
        tractor3.cg_height = tractor2.cg_height
        tractor3.save()
        implement = form_list[3].save()
        other = form_list[4].save()
        tire_coefficient = form_list[5].save()
        soil = form_list[6].save()
        soil_coefficient = form_list[7].save()
        P = tractor3.pto_power
        rpm = tractor3.rpm
        rpm_torque = tractor3.rpm_torque
        T = tractor3.max_torque
        FW = tractor3.front_weight
        RW = tractor3.rear_weight
        L = tractor3.wheelbase
        Hd = tractor3.hitch_point
        Xcgt = tractor3.cg_rear
        Xcgi = Hd -Xcgt
        Wm = implement.weight
        A1 = tire_coefficient.A1
        A2 = tire_coefficient.A2
        A3 = tire_coefficient.A3
        A4 = tire_coefficient.A4
        A5 = tire_coefficient.A5
        A6 = tire_coefficient.A6
        A7 = tire_coefficient.A7
        A8 = tire_coefficient.A8
        rf = tractor3.static_radius_front
        rr = tractor3.static_radius_rear
        br = tractor3.section_width_rear
        bf = tractor3.section_width_front
        dr = tractor3.overall_diameter_rear
        df = tractor3.overall_diameter_front
        CI = soil.cone_index
        Wt = tractor3.front_weight + tractor3.rear_weight
        Yd = 2*other.depth_tillage/300
        Td = other.depth_tillage
        f = soil_coefficient.soil_texture_factor
        A = soil_coefficient.A
        B = soil_coefficient.B
        C = soil_coefficient.C
        Mw = implement.implement_width
        v = other.speed
        bulk_density = soil.bulk_density
        D = f*(A + B*v + C*v*v)*Mw*Td
        eff = 0.77
        s = 0.02
        MR = 0.04
        Py = 0.2 * D
        Rr = ((Wm + Py)*(Xcgi + Hd + L + 0.04*rf)+Wt*(L+0.04*rf -Xcgt) - D*Yd)/(L-0.04*rr + 0.04*rf)
        Rf = Wm + Wt + Py - Rr
        Bn  = (((CI* 1000* br * dr) / (Rr/2)))*((1+A5 * 0.2)/(1+A6 * (br/dr)))
        pro = (A7/Bn) + A4 + A8*s /sqrt(Bn)
        gtr = A1*(1-exp(-A2*Bn))*(1-exp(-A3*s)) +A4
        cot = gtr - pro
        TE = cot*(1-s)/gtr
        Pst = cot*Rr
        Bnr  = (((CI * br * dr) / (Rr)))*((1+A5 * 0.2)/(1+A6 * (br/dr)))
        Bnf  = (((CI * bf * df) / (Rf)))*((1+A5 * 0.2)/(1+A6 * (bf/df)))
        pr = A7/Bnr + A4 +(A8*s/sqrt(Bnr))
        pf = A7/Bnf + A4 +(A8*s/sqrt(Bnf))
        #is eta assumed to be 116 ?
        Pet = (T*116*eff / rr ) - (pro * Rr + 0.04 * Rf)
        # what is WTF and WTI ?
        WTF = Rf - FW
        WTI = Rr-RW - WTF
        while Pet > Pst:
            if D>Pst:
                k = 0
                s = s + 0.001
                Rr = ((Wm + Py)*(Xcgi + Hd + L + 0.04*rf)+Wt*(L+0.04*rf -Xcgt) - D*Yd)/(L-0.04*rr + 0.04*rf)
                Rf = Wm + Wt + Py - Rr
                Bn  = (((CI* 1000* br * dr) / (Rr/2)))*((1+A5 * 0.2)/(1+A6 * (br/dr)))
                pro = (A7/Bn) + A4 + A8*s /sqrt(Bn)
                gtr = A1*(1-exp(-A2*Bn))*(1-exp(-A3*s)) +A4
                cot = gtr - pro
                TE = cot*(1-s)/gtr
                Pst = cot*Rr
                Pet = (T*116 * eff / rr ) - (pro * Rr + 0.04 * Rf)
                print(Pet)
                print(Pst)
                print(D)
            else:
                k = 1
                break
        Ptr = D*v*5/(TE*18)
        Put = (Ptr*100)/(P*1000*(1-0.20))
        #conditions have to be re-examined and tested
        if s <0.08:
            s_out =  "Increase depth or speed of operation slip should not be less than 8%"
        if s > 0.15:
            s_out =  "reduce depth or speed of operation or ballast rear axle of tractor slip should not be greater than 15%"
        if Rf/Wt <0.2:
            Kwef_out =  "reduce depth or speed of operation or ballast rear axle of tractor Front axle weight utilization factor should not be less than 0.2"
        else:
            Kwef_out = "Kwef is in the satisfactory range"
        if s>0.08 and s <0.15:
            s_out =  "Slip is in the satisfactory range" 
 
        if Put>95 and Put<100:
            p_out =  "Tractor is properly loaded"
        elif Put<95:
            p_out =  "Tractor is underloaded"
        elif Put>100:
            p_out = "Tractor is OverLoaded reduce depth or speed of operation"


        return render_to_response('final.html',{'pto':P,'cone_index':CI,'bulk_density':bulk_density,'imp_width':Mw,'depth':Td,'speed':v,'max_pull':Pet,'draft':D,'slip':s*100,'cot':cot,'mrr':pro,'TE':TE,'Krwf':Rr/Wt,'Kfwf':Rf/Wt,'db_power':D*v,'pu':Put,'s_out':s_out,'Kwef_out':Kwef_out,'p_out':p_out},context_instance = RequestContext(self.request))


def sms_reply(self,make,model,implement_name,depth,speed,texture,strength,**kwargs):
    tractor = Tractor.objects.filter(make = make,model = model)[:1]
    implement = Implement.objects.filter(name = implement_name)[:1]
    tire_coefficient = TireCoefficients.objects.filter(tire_type = tractor[0].tire_type)[:1]
    soil = Soil.objects.filter(soil_texture = "Medium",soil_strength = "firm")
    soil_coefficient = SoilCoefficients.objects.filter(soil_texture = texture)
    P = tractor[0].pto_power
    rpm = tractor[0].rpm
    rpm_torque = tractor[0].rpm_torque
    T = tractor[0].max_torque
    FW = tractor[0].front_weight
    RW = tractor[0].rear_weight
    L = tractor[0].wheelbase
    Hd = tractor[0].hitch_point
    Xcgt = tractor[0].cg_rear
    Xcgi = Hd -Xcgt
    Wm = implement[0].weight
    A1 = tire_coefficient[0].A1
    A2 = tire_coefficient[0].A2
    A3 = tire_coefficient[0].A3
    A4 = tire_coefficient[0].A4
    A5 = tire_coefficient[0].A5
    A6 = tire_coefficient[0].A6
    A7 = tire_coefficient[0].A7
    A8 = tire_coefficient[0].A8
    rf = tractor[0].static_radius_front
    rr = tractor[0].static_radius_rear
    br = tractor[0].section_width_rear
    bf = tractor[0].section_width_front
    dr = tractor[0].overall_diameter_rear
    df = tractor[0].overall_diameter_front
    CI = soil[0].cone_index
    Wt = tractor[0].front_weight + tractor[0].rear_weight
    Yd = 2*depth/300
    Td = depth
    f = soil_coefficient[0].soil_texture_factor
    A = soil_coefficient[0].A
    B = soil_coefficient[0].B
    C = soil_coefficient[0].C
    Mw = implement[0].implement_width
    v = speed
    bulk_density = soil[0].bulk_density
    D = f*(A + B*v + C*v*v)*Mw*Td
    eff = 0.77
    s = 0.02
    MR = 0.04
    Py = 0.2 * D
    Rr = ((Wm + Py)*(Xcgi + Hd + L + 0.04*rf)+Wt*(L+0.04*rf -Xcgt) - D*Yd)/(L-0.04*rr + 0.04*rf)
    Rf = Wm + Wt + Py - Rr
    Bn  = (((CI* 1000* br * dr) / (Rr/2)))*((1+A5 * 0.2)/(1+A6 * (br/dr)))
    pro = (A7/Bn) + A4 + A8*s /sqrt(Bn)
    gtr = A1*(1-exp(-A2*Bn))*(1-exp(-A3*s)) +A4
    cot = gtr - pro
    TE = cot*(1-s)/gtr
    Pst = cot*Rr
    Bnr  = (((CI * br * dr) / (Rr)))*((1+A5 * 0.2)/(1+A6 * (br/dr)))
    Bnf  = (((CI * bf * df) / (Rf)))*((1+A5 * 0.2)/(1+A6 * (bf/df)))
    pr = A7/Bnr + A4 +(A8*s/sqrt(Bnr))
    pf = A7/Bnf + A4 +(A8*s/sqrt(Bnf))
    #is eta assumed to be 116 ?
    Pet = (T*116*eff / rr ) - (pro * Rr + 0.04 * Rf)
    # what is WTF and WTI ?
    WTF = Rf - FW
    WTI = Rr-RW - WTF
    while Pet > Pst:
        if D>Pst:
            k = 0
            s = s + 0.001
            Rr = ((Wm + Py)*(Xcgi + Hd + L + 0.04*rf)+Wt*(L+0.04*rf -Xcgt) - D*Yd)/(L-0.04*rr + 0.04*rf)
            Rf = Wm + Wt + Py - Rr
            Bn  = (((CI* 1000* br * dr) / (Rr/2)))*((1+A5 * 0.2)/(1+A6 * (br/dr)))
            pro = (A7/Bn) + A4 + A8*s /sqrt(Bn)
            gtr = A1*(1-exp(-A2*Bn))*(1-exp(-A3*s)) +A4
            cot = gtr - pro
            TE = cot*(1-s)/gtr
            Pst = cot*Rr
            Pet = (T*116 * eff / rr ) - (pro * Rr + 0.04 * Rf)
            print(Pet)
            print(Pst)
            print(D)
        else:
            k = 1
            break
    Ptr = D*v*5/(TE*18)
    Put = (Ptr*100)/(P*1000*(1-0.20))
    #conditions have to be re-examined and tested
    if s <0.08:
        s_out =  "Increase depth or speed of operation slip should not be less than 8%"
    if s > 0.15:
        s_out =  "reduce depth or speed of operation or ballast rear axle of tractor slip should not be greater than 15%"
    if Rf/Wt <0.2:
        Kwef_out =  "reduce depth or speed of operation or ballast rear axle of tractor Front axle weight utilization factor should not be less than 0.2"
    else:
        Kwef_out = "Kwef is in the satisfactory range"
    if s>0.08 and s <0.15:
        s_out =  "Slip is in the satisfactory range" 
 
    if Put>95 and Put<100:
        p_out =  "Tractor is properly loaded"
    elif Put<95:
        p_out =  "Tractor is underloaded"
    elif Put>100:
        p_out = "Tractor is OverLoaded reduce depth or speed of operation"


#    send_kookoo_sms(phone_no='9735483626',message="Testing")
    return p_out

 
