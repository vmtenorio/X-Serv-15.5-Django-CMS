from django.conf.urls import patterns, include, url
from django.contrib import admin
import cms.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'(.*)', cms.views.content, name="Pedir algo a ver si esta en la cache"),
)
