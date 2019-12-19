from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.viewBooks),
    url(r'^add_book$', views.addBook),
    url(r'^add_favorite$', views.addFavorite),
    url(r'^(?P<bookID>\d+)$', views.bookInfo),
    url(r'^del_favorite$', views.delFavorite),
]