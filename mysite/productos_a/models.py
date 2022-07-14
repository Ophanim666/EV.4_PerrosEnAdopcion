from unicodedata import category
from django.db import models

# Create your models here.
CATEGORIAS = (
    ('Alimentos', 'Alimentos'),
    ('Juguetes', 'Juguetes'),
)

class productos_a (models.Model):
    fotografia = models.ImageField(upload_to="images",null=True)
    codigo = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return str(self.fotografia)
