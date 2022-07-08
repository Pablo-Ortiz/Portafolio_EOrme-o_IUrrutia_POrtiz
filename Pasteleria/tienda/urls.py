from django.urls import path
from .views import home, carrito, index, pago, tienda, registro
urlpatterns = [

    path('', index, name="index"),
    path('', home, name="home"),
    path('carrito', carrito, name="carrito"),
    path('tienda', tienda, name="tienda"),
    path('registro', registro, name="registro"),
    path('pago', pago, name="pago"),

    #metodos
]