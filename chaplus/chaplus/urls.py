from django.conf.urls import include, url
from django.contrib import admin
from chaplus import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'chaplus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.mainIndex),
]
