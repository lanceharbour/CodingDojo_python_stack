from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.viewWall),
    url(r'^new_post$', views.newPost),
    url(r'^del_post$', views.delPost),
    url(r'^new_comment$', views.newComment),
    url(r'^del_comment$', views.delComment)
]