# serializers.py
# Aqui vamos a definir que campos vamos a mostrar
# para cada modelo.

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tienda.models import Producto, Cliente, Direccion

class ProductoSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Producto
        fields = ['url', 'id', 'nombre', 'codigo', 
        'precio', 'serie_producto', 'marca', 'img']

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Group
        fields = ['url', 'name']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['url', 'serieCliente', 'nombre', 'rut', 'correo',
                  'id_usuario', 'direccion']

class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = ['url', 'idDireccion', 'calle', 'numero', 'comuna',
                  'region', 'depto']