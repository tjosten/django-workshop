from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # The workshop welcome view
     url(r'^$', 'workshop.views.welcome_view', name='welcome'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Workshop Blog URL Config
    url(r'^blog/', include('blog.urls')),
)

# Automatically serve static files in development setup
urlpatterns += staticfiles_urlpatterns()