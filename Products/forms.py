from django import forms
from .models import Article


class DateInput(forms.DateInput):
    input_type = 'date'


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name_user', 'livraison', 'casse', 'created']
        widgets = {
            #'name_user': forms.Ch(attrs={'class': 'form-control'}),
            'livraison': forms.TextInput(attrs={'class': 'form-control'}),
            'casse': forms.TextInput(attrs={'class': 'form-control'}),
            'created': forms.DateInput(attrs={'class': 'form-control'}),
        }