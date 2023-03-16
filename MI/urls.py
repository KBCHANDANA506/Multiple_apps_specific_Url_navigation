from django.urls import path
from MI.views import *
app_name='MI'
urlpatterns=[
    path('pandya/',pandya,name='pandya'),
    path('rohit/',rohit,name='rohit'),
]