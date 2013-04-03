from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('blog.views',
	url(r'^$', 'main'),
	url(r'^(\d+)/$', 'post'), # links to single post by fk

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
