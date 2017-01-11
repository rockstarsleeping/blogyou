from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^articles/$', views.articles, name="articles"),
    url(r'^like/', views.like_article, name="like_article"),
    url(r'^articles/(?P<article_title_slug>[\w\-]+)/', views.show_article, name='show_article'),

]
