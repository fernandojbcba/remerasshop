from rest_framework import routers
from .viewsets import ProductosViewSet, UsuariosViewSet

router = routers.SimpleRouter()
router.register("api-producto",ProductosViewSet)
router.register("api-usuario",UsuariosViewSet)