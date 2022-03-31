from django.db import models

class Custumer(models.Model):
    name = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    neighborhood = models.CharField(max_length=50, blank=True)  #   bairro
    street = models.CharField(max_length=50, blank=True)
    cellPhone = models.CharField(max_length=50, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):  
        return self.name

    # class Meta:
    #     ordering = ['-updated_at']
    