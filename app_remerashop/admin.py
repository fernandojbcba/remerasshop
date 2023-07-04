from django.contrib import admin

# Register your models here.
from .models import Producto, Usuario
from django.contrib import admin
from .models import Producto, Usuario

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
