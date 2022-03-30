from django import forms


QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)


class CheckoutForm(forms.Form):
    phone_number = forms.CharField(max_length=20, required=True)
    address = forms.CharField(max_length=50, required=True)
