from django.db import models

# Create your models here.
GRADOS_PRODUCTOS = (
    ('Juguete', 'Juguete'),
    ('Alimento', 'Alimento'),
)

class Productos (models.Model):
    fotografia = models.ImageField(upload_to='productos')
    nombre = models.CharField(max_length=50)
    # precio = models.IntegerField()  
    grado_productos = models.CharField(max_length=50, choices=GRADOS_PRODUCTOS)

    def __str__(self):
        return str(self.fotografia)
