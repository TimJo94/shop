from decimal import Decimal

from django.db import models
from django.contrib.auth import get_user_model
from main.models import Product

User = get_user_model()


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = {}
            self.session['cart'] = {}
        self.cart = cart

    # {'1': {'quantity':2, 'price': 10000}}
    def add(self, product_id, quantity, price):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': price
            }
            self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for prod in products:
            self.cart[str(prod.id)]['product'] = prod
        for item in self.cart.values():
            item['item_total'] = Decimal(item['price']) * item['quantity']
            yield item

    def get_cart_total(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def increment_quantity(self, product_id):
        product_id = str(product_id)
        print(product_id)
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] < 20:
                self.cart[product_id]['quantity'] += 1
                self.save()

    def clear(self):
        del self.session['cart']
        self.session.modified = True



STATUS_CHOICES = (
    ('open', 'Открытый'),
    ('in_process', 'В обработке'),
    ('cancel', 'Отменённый'),
    ('finished', 'Завершённый')
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderItems')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')

    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='order_items')

    quantity = models.PositiveSmallIntegerField(default=1)














