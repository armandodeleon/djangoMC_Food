from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item  # model to use in the form
        fields = '__all__'  # all the fields should be used
