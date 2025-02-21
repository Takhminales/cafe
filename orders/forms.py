from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items']

    def clean_items(self):
        """Проверка на корректность списка блюд."""
        items = self.cleaned_data['items']
        if not isinstance(items, list):
            raise forms.ValidationError("Список блюд должен быть в формате JSON.")
        return items
