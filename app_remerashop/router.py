from rest_framework import routers
from .viewsets import ProductosViewSet

router = routers.SimpleRouter()
router.register("api-producto",ProductosViewSet)