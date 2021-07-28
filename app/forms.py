from .models import Products
from django import forms 


class ProductsForm(forms.ModelForm):
	class Meta :
		model = Products
		fields = "__all__"