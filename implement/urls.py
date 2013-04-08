from django.conf.urls import patterns,include,url 

from models import *
from views import DSSWizard

urlpatterns = patterns('',
    (r'^tractor/form/$',DSSWizard.as_view([BasicTractorForm, AdvancedTractorForm, TireForm, ImplementForm, OtherForm, TireCoefficientsForm,SoilForm, SoilCoefficientsForm, ]),),
)
