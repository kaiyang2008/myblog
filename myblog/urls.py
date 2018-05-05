from django.conf.urls import include, url
from django.contrib import admin
from mainsite.views import homepage

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'myblog.views.hello',name='hello'),
    url(r'^$', homepage)
]
