from django.conf.urls import patterns, include, url
from rapidsms.backends.kannel.views import KannelBackendView

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
    # Kannel Urls
     url(r'^backend/kannel-fake-smsc/$',KannelBackendView.as_view(backend_name = "kannel-fake-smsc")),
     url(r'^backend/kannel-usb0-smsc/$',KannelBackendView.as_view(backend_name = "kannel-usb0-smsc")),
#    url(r'kannel/',include('rapidsms.backends.kannel.urls')),
 
    # RapidSMS core URLs
    (r'^accounts/', include('rapidsms.urls.login_logout')),
    url(r'^$', 'rapidsms.views.dashboard', name='rapidsms-dashboard'),
    # RapidSMS contrib app URLs
    (r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    #(r'^locations/', include('rapidsms.contrib.locations.urls')),
    (r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
    (r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    (r'^registration/', include('rapidsms.contrib.registration.urls')),
)
