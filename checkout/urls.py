from django.urls import path
from . import views
# copied and modified from homeapp urls.py
urlpatterns = [
    path('', views.checkout, name='checkout')
]
