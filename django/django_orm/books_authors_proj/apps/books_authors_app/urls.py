from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.authors),
    url(r'^books/(?P<number>\d+)$', views.displayBookInfo),
    url(r'^authors/(?P<number>\d+)$', views.displayAuthorInfo),
    url(r'^add_book$',views.addBook),
    url(r'^add_author$',views.addAuthor),
    url(r'^add_authortobook$',views.addAuthorToBook),
    url(r'^add_booktoauthor$',views.addBookToAuthor)
]