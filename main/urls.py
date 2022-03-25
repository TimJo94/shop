from django.urls import path

from main.views import ProductDetailsView, ProductsListView, CreateProductView, UpdateProductView, DeleteProductView, \
    SearchResultsView

urlpatterns = [
    path('search', SearchResultsView.as_view(), name='search-results'),
    path('create/', CreateProductView.as_view(), name='create-product'),
    path('<slug:category_id>/', ProductsListView.as_view(), name='products-list'),
    path('details/<int:pk>/', ProductDetailsView.as_view(), name='product-details'),
    path('update/<int:pk>/', UpdateProductView.as_view(), name='update-product'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete-product'),

]