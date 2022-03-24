from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View

from main.models import Product
from order.forms import AddToCartForm
from order.models import Cart


class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
            cart.add(product.id, quantity, str(product.price))
        return redirect(reverse_lazy('cart-details'))


class RemoveFromCartView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product_id)
        return redirect(reverse_lazy('cart-details'))


class CartDetailsView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'order/cart_details.html', {'cart': cart})


class IncrementQuantityView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product_id = get_object_or_404(Product, id=product_id)
        cart.increment_quantity(product_id)
        return redirect(reverse_lazy('cart-details'))




