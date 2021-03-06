from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index_page'),
    path('login/', views.signin, name ="signin"),
    path('dashbord/',views.dashbord, name="dash"),
    path('signout/',views.signout,name="signout"),
    path('up_video/',views.up_video, name="upload_video"),
    path('cmt_upld/', views.cmt_upld, name='cmt_upload')
]
