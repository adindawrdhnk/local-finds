from django import forms
from .models import Product
from django.utils.html import strip_tags

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "origin", "rating", "discount"]
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(str(price)) 

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_stock(self):
        stock = self.cleaned_data["stock"]
        return strip_tags(str(stock))  

    def clean_origin(self):
        origin = self.cleaned_data.get("origin", "")
        return strip_tags(origin)

    def clean_rating(self):
        rating = self.cleaned_data.get("rating", "")
        return strip_tags(str(rating)) 

    def clean_discount(self):
        discount = self.cleaned_data.get("discount", "")
        return strip_tags(str(discount)) 
