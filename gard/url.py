from . import views
import django.urls as urls
from django.urls import path,include
urlpatterns=[
path('',views.index,name='index')
]