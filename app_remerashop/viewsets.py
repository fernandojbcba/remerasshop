from rest_framework.viewsets import ModelViewSet
from .models import Producto,Usuario
from .serializers import ProductoSerializer, UsuarioSerializer

class ProductosViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class UsuariosViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer