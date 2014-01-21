from django.conf.urls.defaults import patterns, include, url
from views import start, body_calendar, calendar_xml, test_xml

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', start),
     url(r'^kalendar/', body_calendar),
     url(r'^calendar_xml/', calendar_xml),
     url(r'^test_xml/', test_xml),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)