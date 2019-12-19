from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'shows$', views.shows),
    url(r'shows/new$', views.newShow),
    url(r'shows/create$', views.addShow),
    url(r'shows/(?P<showID>\d+)$', views.showInfo),
    url(r'shows/(?P<showID>\d+)/edit$', views.editShow),
    url(r'shows/(?P<showID>\d+)/update$', views.updateShow),
    url(r'shows/(?P<showID>\d+)/destroy$', views.destroyShow),
]