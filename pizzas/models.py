from django.db import models
from django.conf import settings

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    desciption = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    # Utiliza una ruta relativa para el campo ImageField
    image = models.ImageField(upload_to='img/pizzas/', null=True, blank=True)

    def __str__(self):
        return self.name