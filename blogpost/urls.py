from django.urls import path
from .views import *


urlpatterns=[
    path('',homepage,name="home"),
    path('blogpage/',blogpage,name="blogpage"),
    path('blog/<str:blogid>/',blog,name="blog"),
    path('about/',aboutpage,name="about"),
    path('contact/',contactpage,name="contact"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('addcomment/<str:id>/',addcomment,name="addcomment"),
    # path('delete/<str:id>/<str:cmtid>',delete_comment,name="delete"),
    path('presslike/<str:id>/',presslike,name="presslike"),
    path('pressclike/<str:postid>/<str:commentid>/',press_c_likes,name="pressclike"),


]

