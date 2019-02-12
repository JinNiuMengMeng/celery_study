from django.conf.urls import include, url
from django.contrib import admin
from course import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'imooc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^do/$', views.do, name='do'),
]
