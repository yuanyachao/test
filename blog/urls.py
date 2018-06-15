
from django.conf.urls import url,include
from django.contrib import admin


from blog import views





urlpatterns = [

    #url(r'^(?P<article_type_id>\d+)/', views.index),
    url("(?P<user_site>\w+)/article/(?P<article_id>\d+)",views.articleDetail),

    url("(?P<user_site>\w+)/article/(?P<condition>category|tag|date)/(?P<para>\w+)",views.homeSite),

    url("poll/$",views.poll),
    url("comment/$",views.comment),

    url("(?P<user_site>\w+)",views.homeSite),# homeSite(request,user_site)





]
