from django.db import models

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.titulo
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre