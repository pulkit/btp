from django.conf.urls import patterns,include,url 

urlpatterns = patterns('',
	url(r'^tractor/query$','implement.views.query'),
	url(r'^tractor/create$','implement.views.create'),

)
