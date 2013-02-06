from django.conf.urls import patterns,include,url 

from implement.models import *
from implement.views import DSSWizard

urlpatterns = patterns('',
    (r'^tractor/form/$',DSSWizard.as_view([BasicTractorForm, AdvancedTractorForm, TireForm, ImplementForm, OtherForm, TireCoefficientsForm,SoilForm, SoilCoefficientsForm, ]),),
)
