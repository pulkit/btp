from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dss.views.home', name='home'),
    url(r'^dss/', include('implement.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),




    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
                  'document_root': settings.STATIC_ROOT,
      }),
      # RapidSMS core URLs
     
     (r'^accounts/', include('rapidsms.urls.login_logout')),
     url(r'^$', 'rapidsms.views.dashboard', name='rapidsms-dashboard'),
     
     # RapidSMS contrib app URLs
     
     (r'^httptester/', include('rapidsms.contrib.httptester.urls')),
     
     #(r'^locations/', include('rapidsms.contrib.locations.urls')),
     
     (r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
     (r'^messaging/', include('rapidsms.contrib.messaging.urls')),
     (r"^selectable/", include("selectable.urls")),

     (r'^registration/', include('rapidsms.contrib.registration.urls')),
)
