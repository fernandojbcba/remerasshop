from django.db import models

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f"El producto: {self.titulo}, categoria {self.categoria},precio {self.precio} "
    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ] 
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ] 