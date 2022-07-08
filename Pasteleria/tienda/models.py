from distutils.command.upload import upload
from mailbox import NoSuchMailboxError
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone

# Create your models here.
class Producto(models.Model) :
    serie_producto = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=15)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField()
    img = models.ImageField(upload_to='img', null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.nombre


class Direccion(models.Model):
    idDireccion = models.CharField(max_length=30)
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()
    comuna = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    depto = models.CharField(max_length=30)

    def __str__(self) :
        return self.calle

class Cliente(models.Model):
    serieCliente = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)
    id_usuario = models.CharField(max_length=10)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=150, unique=True)

    USERNAME_FIELD = 'email'  # new

    REQUIRED_FIELDS = ['username', 'password']  # new