
from django.shortcuts import render, HttpResponse
from .models import Thunder

def inicio(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    return render(request,"home.html")


def registrar(request):
    Thunder.objects.create(
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    dv = request.POST['dv'],
    email = request.POST['email'],
    password = request.POST['password'],
    direccion = request.POST['direccion']
    )
    return render(request,"home.html")

def leer(request):
    clientes = Thunder.objects.all()
    # ^ equivalente a select * from Thunder
    return render(request,"home.html")

def actualizar(request):
    id = request.POST['id']
    cliente = Thunder.objects.get(id=id)
    errores = Thunder.objects.validador_cliente(request.POST)

    if len(cliente) > 0:
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.rut = request.POST['rut']
        cliente.dv = request.POST['dv']
        cliente.email = request.POST['email']
        cliente.password = request.POST['password']
        cliente.direccion = request.POST['direccion']
