from django.urls import path
from app1.views import *
app_name='nothing'
urlpatterns=[path('httpRes/',httpRes,name='httpRes')]