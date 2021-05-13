from django.shortcuts import( 
    render, redirect
    )

# Create your views here.


def view_basket(request):
    """ A view to renders the basket content page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ add a quantity of specified products to shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    """ add the basket varible if exist in session or create it """
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = basket.get(item_id, 0) + quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
