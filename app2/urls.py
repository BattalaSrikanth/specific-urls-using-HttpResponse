from django.urls import path
from app2.views import *
app_name='puli2'

urlpatterns=[
    path('function2/',function2,name='function2'),
]