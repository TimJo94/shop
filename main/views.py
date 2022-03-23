from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Category, Product
from .forms import CreateProductForm, UpdateProductForm


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


#доступ только для администраторов
class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_staff


class CreateProductView(IsAdminCheckMixin, CreateView):
    queryset = Product.objects.all()
    template_name = 'main/create_product.html'
    form_class = CreateProductForm

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(reverse_lazy('product-details', args=[product.id]))
        return self.form_invalid(form)


class UpdateProductView(IsAdminCheckMixin, UpdateView):
    queryset = Product.objects.all()
    template_name = 'main/update_product.html'
    form_class = UpdateProductForm

    def get_success_url(self):
        product_id = self.kwargs.get('pk')
        return reverse_lazy('product-details', args=[product_id])


class DeleteProductView(IsAdminCheckMixin, DeleteView):
    queryset = Product.objects.all()
    template_name = 'main/delete_product.html'
    success_url = reverse_lazy('index')



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
