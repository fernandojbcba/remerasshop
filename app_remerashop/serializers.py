from rest_framework.serializers import ModelSerializer
from .models import Producto, Usuario

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"