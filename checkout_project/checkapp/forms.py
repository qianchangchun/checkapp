from django import forms
from checkapp.models import Computer

class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Computer
        fields = ('name', 'is_available')
