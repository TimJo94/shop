from django.urls import path

from order.views import AddToCartView, RemoveFromCartView, CartDetailsView, IncrementQuantityView, PlaceOrderView, \
    OrdersListView

urlpatterns = [
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/details/', CartDetailsView.as_view(), name='cart-details'),
    path('cart/increment/<int:product_id>/', IncrementQuantityView.as_view(), name='increment-quantity'),
    path('checkout/', PlaceOrderView.as_view(), name='checkout'),
    path('orders/', OrdersListView.as_view(), name='orders-list')

]