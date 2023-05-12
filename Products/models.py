from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.

class Article(models.Model):
    name_user = models.ForeignKey(User, on_delete=models.CASCADE)
    livraison = models.IntegerField()
    casse = models.IntegerField()
    ensache = models.IntegerField(null=True)
    tx_casse = models.FloatField(null=True)
    created = models.DateField()

    class Meta:
        verbose_name = ('Article')
        verbose_name_plural = ('Article')

    """ def make_ensache(self):
        self.ensache = self.livraison * 20
    def save(self, *args, **kwargs)->None:
        self.make_ensache()
        return super().save(*args, **kwargs) """
    
    @property
    def ensache(self):
        ensache = self.livraison * 20
        return ensache

    def make_tx_casse(self):
        self.tx_casse = (self.casse * 100)/(self.ensache + self.casse)
    def save(self, *args, **kwargs)->None:
        self.make_tx_casse()
        return super().save(*args, **kwargs)
    
    