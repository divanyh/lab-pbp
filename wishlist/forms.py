from statistics import mode
from django import forms
from wishlist.models import BarangWishlist

class AddBarangForm(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        fields = "__all__"

        widgets = {
            'name' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control'}),
            'price' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'type' : 'textarea', 'class' : 'form-control'})
        }

        name = forms.CharField(label = 'Name', required = True, widget = widgets['name'])
        price = forms.CharField(label = 'Price', required = True, widget = widgets['price'])
        description = forms.CharField(label = 'Description', required = True, widget = widgets['description'])
