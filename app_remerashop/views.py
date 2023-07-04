# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Producto



class ProductosBaseView(View):
    template_name = 'productos.html'
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('Producto:all')


class ProductosListView(ProductosBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS productos
    """

class ProductosDetailView(DetailView):
    model = Producto
    template_name = 'productos_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto = self.get_object()
        fields = producto._meta.get_fields()

        context['fields'] = fields
        return context

class ProductosCreateView(ProductosBaseView,CreateView):
    template_name = "productos_create.html"
    extra_context = {
        "tipo": "Crear producto"
    }


class ProductosUpdateView(ProductosBaseView,UpdateView):
    template_name = "productos_create.html"
    extra_context = {
        "tipo": "Actualizar producto"
    }

class ProductosDeleteView(ProductosBaseView,DeleteView):
    template_name = "productos_delete.html"
    extra_context = {
        "tipo": "Borrar producto"
    }