from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import Usuario
from .models import Rescatado
from django.http import  HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout, login as login_user
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.

def index(request):
    return render(request,'index.html',{'nombre':"Edgar"})

def form(request):
    return render(request,'form.html',{})

def crear(request):
    nombre = request.POST.get('nombre','')
    return HttpResponse("nombre' : " + nombre)

def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")

def logearse(request):
    nombre = request.POST.get("usuario",False)
    contrasenia = request.POST.get("contrasenia",False)
    user = authenticate(request, username=nombre, password=contrasenia)
    print(nombre,contrasenia)
    print(user)
    if user is not None:
        login_user(request, user)
        return redirect("index")
    else:
        messages.error(request,'El usuario o la contraseña no es válido ')
        return redirect("inicio")

def inicio(request):
    return render(request,'inicio.html',{})

def form_rescatado(request):
    return render(request,'form_rescatado.html',{})

def crear_rescatado(request):
    foto = request.FILES['foto']
    nombre = request.POST.get('nombre', '')
    raza = request.POST.get('raza', '')
    descripcion = request.POST.get('descripcion', '')
    estado = request.POST.get('estado', 1)
    perro = Rescatado(foto=foto,nombre=nombre,raza=raza,descripcion=descripcion,estado=estado)
    print(perro.foto)
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

def buscar(request):
    num_estado = request.POST.get('estado',0)
    perritos = Rescatado.objects.filter(estado=num_estado)
    return render(request,'buscar.html',{'perritos':perritos})

def crear_persona(request):
    nombres = request.POST.get('Nombres', '')
    apellidos = request.POST.get('Apellidos', '')
    rut = request.POST.get('rut', '')
    email = request.POST.get('Correo', '')
    fechaNacimiento = request.POST.get('Fecnac', '1912-01-01')
    telefono = request.POST.get('NTel', 11111111)
    tipoCasa = request.POST.get('exampleFormControlSelect2', '')
    region = request.POST.get('regiones', '')
    comuna = request.POST.get('comunas', '')
    persona = Usuario(nombres=nombres,apellidos=apellidos,rut=rut,email=email,fechaNacimiento=fechaNacimiento,
    telefono=telefono,tipoCasa=tipoCasa,region=region,comuna=comuna)
    persona.save()
    return HttpResponse("Usuario "+nombres+" "+apellidos+", ha sido registrado")

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password.html', {
        'form': form
    })


def administrador(request):
    return render(request,'administrador.html',{})