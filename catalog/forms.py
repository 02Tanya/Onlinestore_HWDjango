from django import forms

from catalog.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def clean_name(self):
        '''Валидация содержимого наименования продукта'''
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['name']

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('Такое название для продукта недопустимо')

        return cleaned_data

    def clean_description(self):
        '''Валидация описания продукта'''
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        cleaned_data = self.cleaned_data['description']

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('Такое описание для продукта недопустимо')

        return cleaned_data



