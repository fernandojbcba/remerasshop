from django.views.generic import TemplateView

class landing(TemplateView):
    template_name= "page/landing_pages.html"
    

class carrito(TemplateView):
    template_name= "page/carrito.html"
    

class contacto(TemplateView):
    template_name= "page/contacto.html"
    

class login(TemplateView):
    template_name= "page/login.html"
  

class quienessomos(TemplateView):
    template_name= "page/quienessomos.html"
   
class tienda(TemplateView):
    template_name= "page/tienda.html"
       