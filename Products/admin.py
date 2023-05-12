from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    fields = ['name_user', 'livraison', 'casse', 'created']
    list_display = ('id', 'name_user', 'livraison', 'casse', 'ensache', 'tx_casse', 'created')

    """ def tx_casse(self, obj):
        if obj.cass:
            return (obj.cass * 100) // (obj.ensache + obj.casse)
        else: 
            return '-' """
