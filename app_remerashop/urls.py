from django.contrib import admin
from django.urls import path , include
from .router import router 

from .views import      ProductosListView   \
                    ,   ProductosDetailView \
                    ,   ProductosCreateView \
                    ,   ProductosUpdateView \
                    ,   ProductosDeleteView \
                    

app_name = "productos"

urlpatterns = [
    path("", ProductosListView.as_view(), name="all"),
    path("create/", ProductosCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", ProductosDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", ProductosUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ProductosDeleteView.as_view(), name="delete"),


]
urlpatterns += router.urls