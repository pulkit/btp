from django.conf.urls import patterns,include,url 

from implement.models import TractorForm,TireForm
from implement.views import DSSWizard

urlpatterns = patterns('',
#	url(r'^tractor/create$','implement.views.create'),
    url(r'^tractor/form/$',DSSWizard.as_view([TractorForm, TireForm])),
)
