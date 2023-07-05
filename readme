***
## objetivos de este TFI
***
#### Utilizar la implementación de django views para generar las rutas y colocar los endpoints necesarios para que internamente reconozca los paths  que el proyecto requiere.
 ```
 rutas : 
 urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing.as_view(), name='landing'),
    path('carrito/', carrito.as_view(), name='carrito'),
    path('contacto/', contacto.as_view(), name='contacto'),
    path('login/', login.as_view(), name='login'),
    path('quienessomos/', quienessomos.as_view(), name='quienessomos'),
    path('tienda/', tienda.as_view(), name='tienda'),
    path("productos/", include("app_remerashop.urls")),

]
views: 
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

 ```
  ## Levantar los archivos estáticos que se necesitaron para la parte funcional y estética del proyecto.
```{% load static %}```
 ``` <link rel="stylesheet" href="{% static 'css/styles.css' %}" /> ```
 ```   <link rel="stylesheet" href="{% static 'css/login.css' %}" /> ```
 ``` <script src="{% static './js/menu.js' %}"></script> ```

## Generar un CRUD con los apps de django, e integrarlo con el front de django.
-  http://remerashop.pythonanywhere.com/productos/
## se generaron los api-rest 
-  http://remerashop.pythonanywhere.com/productos/api-usuario
- http://remerashop.pythonanywhere.com/productos/api-producto
## Hacer un deploy en python anywhere
-  http://remerashop.pythonanywhere.com
## se integro con base datos mysql
```
DATABASES = {
'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'remerashop$remerashop',
            'USER': 'remerashop',
            'PASSWORD': 'Argentina2023',
            'HOST': 'remerashop.mysql.pythonanywhere-services.com',
            'PORT': '3306',
            'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
        }
}
```