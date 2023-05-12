from django import forms
from .models import Article


class DateInput(forms.DateInput):
    input_type = 'date'


class ArticleForm(forms.ModelForm):
    #category = forms.ChoiceField()
    livraison = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    casse = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #ensache = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    created = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))


    class Meta:
        model = Article
        fields = ('name_user', 'livraison', 'casse', 'created')