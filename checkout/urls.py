from django.urls import path
from . import views
# copied and modified from homeapp urls.py
urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]
