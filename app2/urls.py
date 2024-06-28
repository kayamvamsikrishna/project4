from django.urls import path
from app2.views import *
app_name='nothings'
urlpatterns=[path('hPage/',hPage,name='hPage')]