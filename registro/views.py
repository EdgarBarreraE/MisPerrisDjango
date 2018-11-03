from django.shortcuts import render
from django.http import  HttpResponse
from .models import Usuario
from .models import Rescatado

# Create your views here.

def index(request):
    return render(request,'index.html',{'nombre':"Edgar"})

def form(request):
    return render(request,'form.html',{})

def crear(request):
    nombre = request.POST.get('nombre','')
    return HttpResponse("nombre' : " + nombre)

def Inicio(request):
    return render(request,'Inicio.html',{})

def form_rescatado(request):
    return render(request,'form_rescatado.html',{})

def crear_rescatado(request):
    foto = request.FILES['foto']
    nombre = request.POST.get('nombre', '')
    raza = request.POST.get('raza', '')
    descripcion = request.POST.get('descripcion', '')
    estado = request.POST.get('estado', 1)
    perro = Rescatado(foto=foto,nombre=nombre,raza=raza,descripcion=descripcion,estado=estado)
    perro.save()
    return HttpResponse("El perrito "+nombre+" de raza "+raza+", ha sido correctamente registrado")

def lista_rescatados(request):
    return render(request,'lista_rescatados.html',{'elementos':Rescatado.objects.all()})

def editar(request,id):
    perro = Rescatado.objects.get(pk=id)
    return render(request,'editar.html',{'perro':perro})

def editado(request,id):
    perro = Rescatado.objects.get(pk=id)
    foto = request.FILES['foto']
    nombre = request.POST.get('nombre', '')
    raza = request.POST.get('raza', '')
    descripcion = request.POST.get('descripcion', '')
    estado = request.POST.get('estado', 1)
    perro.nombre = nombre
    perro.raza = raza
    perro.descripcion = descripcion
    perro.estado = estado
    perro.foto = foto
    perro.save()
    return HttpResponse("El perrito "+nombre+" ha sido sido editado")


def eliminar(request,id):
    perro = Rescatado.objects.get(pk=id)
    perro.delete()
    return HttpResponse("Perrito ha sido eliminado de los registros.")
