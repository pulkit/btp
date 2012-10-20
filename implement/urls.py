from django.conf.urls import patterns,include,url 

urlpatterns = patterns('',
	url(r'^dss/$','implement.views.Tractor'),
)
