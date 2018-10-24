from django.shortcuts import render
from django.http import  HttpResponse

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