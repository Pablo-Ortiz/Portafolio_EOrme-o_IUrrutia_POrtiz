from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from tienda.Carrito import Carrito
from tienda.models import Producto
from tienda.forms import CustomUserCreationForm
import mercadopago


def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    url = 'http://127.0.0.1:8000/manage/productos/' 
    response = requests.get(url, auth = ('admin', 'duoc'))
    data = response.json()
    productos = {'productos': data}
    return render(request,'tienda.html', productos)

def guardar(request):
    carrito = Carrito(request)
    carrito.guardar_carrito()
    return redirect("tienda")

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def sumar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")
    
def pago(request):
    sdk = mercadopago.SDK("TEST-3031510683130060-051002-5c2361b8d4611687c2a9166ae54ec4a2-634882159")

    payment_methods_response = sdk.payment_methods().list_all()
    payment_methods = payment_methods_response["response"]
    return render(request, "pago.html")

def enviar_pago(request):
    import mercadopago
    sdk = mercadopago.SDK("ACCESS_TOKEN")
 
    payment_data = {
    "transaction_amount": float(request.POST.get("transaction_amount")),
    "token": request.POST.get("token"),
    "description": request.POST.get("description"),
    "installments": int(request.POST.get("installments")),
    "payment_method_id": request.POST.get("payment_method_id"),
    "payer": {
        "email": request.POST.get("email"),
        "identification": {
            "type": request.POST.get("type"), 
            "number": request.POST.get("number")
        }
    }
    }
 
    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
 
    print(payment)

def producto_search(request):
    texto_de_busqueda = request.GET["texto"]
    return render(request, 'search.html',{
        'texto_buscado' : texto_de_busqueda,
    })

# Create your views here.

def home(request):
    return render(request, 'index.html')

def carrito(request):
    return render(request, 'carrito.html')

def index(request):
    return render(request, 'index.html')

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method =='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="home")
        data["form"]=formulario
    return render(request,'registration/registro.html',data)

def log_in(request):
    return render(request, 'registration/login.html')

