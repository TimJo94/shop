from order.forms import AddToCartForm
from main.models import Category


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def get_cart_form(request):
    cart_form = AddToCartForm()
    return {'cart_form': cart_form}