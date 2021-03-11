from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index_page'), #registration page
    path('login/', views.signin, name ="signin"), #login page
    path('dashbord/',views.dashbord, name="dash"), #dashbord
    path('signout/',views.signout,name="signout"), #signout and redirect to registration page
    path('up_video/',views.up_video, name="upload_video"), #upload video 
    path('cmt_upld/', views.cmt_upld, name='cmt_upload'), #comment upload logic and redirect to dashbord
    path('like_l/',views.like_l,name="like"),
    path('unlike/<msg>/',views.unlike,name="unlike")

]
