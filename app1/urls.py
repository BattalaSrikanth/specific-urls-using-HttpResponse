from django.urls import path
from app1.views import *
app_name='puli1'

urlpatterns=[
    path('function1/',function1,name='function1')
]