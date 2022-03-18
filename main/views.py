from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product


def index_page(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})





# TODO: сделать список продуктов
# TODO: авторизация
# TODO: фильтрация, поиск, пагинация
# TODO: корзина
# TODO: заказы
# TODO: отправка писем
# TODO: деплой
# TODO: верстка
