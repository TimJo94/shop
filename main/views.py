from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from order.forms import AddToCartForm
from .models import Category, Product
from .forms import CreateProductForm, UpdateProductForm


def index_page(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})


class ProductsListView(View):
    def filter_queryset(self, products):
        price_from = self.request.GET.get('price_from', 0)
        price_to = self.request.GET.get('price_to', 0)
        if price_from and price_from.isdigit():
            products = products.filter(price__gte=price_from)
        if price_to and price_to.isdigit():
            products = products.filter(price__lte=price_to)
        return products

    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id)
        products = self.filter_queryset(products)
        products = self.paginate_queryset(products)
        cart_form = AddToCartForm()
        return render(request, 'main/products_list.html', {'products': products, 'cart_form': cart_form})

    def paginate_queryset(self, products):
        page_number = self.request.GET.get('page')
        paginator = Paginator(products, 3)
        try:
            page = paginator.page(page_number)
        except InvalidPage:
            page = paginator.page(1)
        return page



class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'main/product_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cart_form'] = AddToCartForm()
        return context


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


class SearchResultsView(ListView):
    queryset = Product.objects.all()
    template_name = 'main/search_results.html'
    context_object_name = 'products'

    def get_queryset(self):
        q = self.request.GET.get('q')
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
        # select * from product where name ilike'%q%' OR description ilike '%q%';
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        # context is data that you pass from views into html
        context['cart_form'] = AddToCartForm()
        return context


# class ProductsListView(ListView):
#     queryset = Product.objects.all()
#     template_name = 'main/products_list.html'


# TODO: фильтрация, поиск, пагинация
# TODO: заказы
# TODO: отправка писем
# TODO: деплой
# TODO: верстка
