from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ensachage(models.Model):
    """Model definition for MODELNAME."""
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    livraison = models.IntegerField(blank=True, null=True, default=0)
    casse = models.IntegerField(blank=True, null=True, default=0)
    ensache = models.IntegerField(blank=True, null=True)
    tx_casse = models.FloatField(blank=True, null=True)
    vrac = models.FloatField(blank=True, null=True, default=0)
    created = models.DateField(blank=False)   

    # TODO: Define fields here

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Ensachage'
        verbose_name_plural = 'Ensachage'
        
    def __str__(self) -> str:
        if self.tx_casse:
            self.tx_casse= round(self.tx_casse, 2)
        return super().__str__()
    
    # def __str__(self) -> str:
    #     if self.livraison==0 and self.casse==0:
    #         self.tx_casse= 0
    #     return super().__str__()
    
    
    def make_ensache(self):
        if self.livraison is not None and self.casse is not None:
            self.ensache = self.livraison * 20
        
   
    def make_tx_casse(self):
        if self.ensache != 0 and self.casse != 0:
            self.tx_casse = (self.casse * 100)/(self.ensache + self.casse)
        else:
            self.tx_casse = 0
        
    def save(self, *args, **kwargs)->None:
        self.make_ensache()
        self.make_tx_casse()
        return super().save(*args, **kwargs)
