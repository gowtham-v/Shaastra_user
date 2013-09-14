from users import views
from django.conf.urls.defaults import patterns, include,url
from misc.dajaxice.core import dajaxice_autodiscover
from django.conf import settings
from misc.dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('misc.dajaxice.urls')),
    # Examples:
    # url(r'^$', 'Test2k14_Personalised_Profile.views.home', name='home'),
    # url(r'^Test2k14_Personalised_Profile/', include('Test2k14_Personalised_Profile.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('users.urls')), 
    #(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    
    )
