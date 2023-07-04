from rest_framework.viewsets import ModelViewSet
from .models import Producto
from .serializers import ProductoSerializer

class ProductosViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer