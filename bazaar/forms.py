from django import forms
from .models import SaleProduct

class ProductBuyForm(forms.ModelForm):
	class Meta:
			model = SaleProduct
			fields=[]