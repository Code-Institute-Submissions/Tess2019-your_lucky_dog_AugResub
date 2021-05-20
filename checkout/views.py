from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in yout´r basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = { 
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ItF0wCgSnLukhN2UgqzkPQgvAa0KwvFkHZxRh93APvEYT4zGkKINQftUcXhzT1mq9mCFPtefXL2XEzQOZpUWkuI00wa47R8DN',
        'client_secret':'test client secret',
        }

    return render(request, template, context) 
