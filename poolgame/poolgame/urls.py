from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'brbappl.views.index', name='index'),
    url(r'^done$', 'brbappl.views.done', name='done'),
    url(r'^participate$', 'brbappl.views.participate', name='participate'),
    url(r'^admin', include(admin.site.urls)),
    url(r'^(?P<contestant>\w+)$', 'brbappl.views.questionnaire', name='questions'),
    # url(r'^poolgame/', include('poolgame.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
