from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .favorites import Favorites
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm

@login_required
def favs_add(request, product_id):
    favs = Favorites(request)
    product = get_object_or_404(Product, id=product_id)  
    product.is_favorite = True
    product.save()
    favs.add(product)
    cart_product_form = CartAddProductForm()
    # return render('favorites:favs_list')
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

@login_required
def favs_remove(request, product_id):
    favs = Favorites(request)
    product = get_object_or_404(Product, id=product_id)
    product.is_favorite = False
    product.save()
    favs.remove(product)
    cart_product_form = CartAddProductForm()
    # return redirect('favorites:favs_list')
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

@login_required
def favs_list(request):
    favs = Favorites(request)
    if favs.size() == 0:
        for p in Product.objects.all():
            if p.is_favorite:
                favs_add(request,p.id)
    return render(request, 'favorites/details.html', {'favs': favs})