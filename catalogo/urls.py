from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^single/(?P<sku>[0-9]+)/$', views.single, name='single'),
    url(r'^categoria/(?P<id>[0-9]+)/$', views.categoria, name='categoria'),
]
