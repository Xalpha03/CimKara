from django.contrib import admin
from .models import *
# Register your models here.

class AdminEnsachage(admin.ModelAdmin):
    '''Admin View for '''
    model = Ensachage
    fields = ['username', 'livraison', 'casse', 'vrac', 'created']
    list_display = ('username', 'livraison', 'casse', 'ensache', 'tx_casse', 'vrac', 'created')
    list_filter = ('username', 'created')
    readonly_fields = ('ensache', 'tx_casse', )
    search_fields = ('created',)
    ordering = ('-id',)
admin.site.register(Ensachage, AdminEnsachage)