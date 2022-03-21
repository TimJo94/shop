from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Category, Product


def index_page(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})


class ProductsListView(View):
    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id)
        return render(request, 'main/products_list.html', {'products': products})


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'main/product_details.html'

# class ProductsListView(ListView):
#     queryset = Product.objects.all()
#     template_name = 'main/products_list.html'

# TODO: сделать переходы между страницами
# TODO: сделать список продуктов
# TODO: авторизация
# TODO: фильтрация, поиск, пагинация
# TODO: корзина
# TODO: заказы
# TODO: отправка писем
# TODO: деплой
# TODO: верстка
