from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from .formularios.registerform import NewUserForm
from .formularios.loginform import LoginForm
from .models import Produtos, Proovedores


def proveedoresList(request):
    proveedores = Proovedores.objects.all()
    return render(request,"prov.html",{'proveedores':proveedores})

def es_admin(user):
   return user.is_staff

@user_passes_test(es_admin)
def agregarProveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        proveedor = Proovedores(nombre=nombre, telefono=telefono)
        proveedor.save()
        return redirect('proveedores_list.html')

    return render(request, "agregar_proveedor.html")

def productosList(request):
    productos = Produtos.objects.all()
    return render(request,"produc.html",{'productos':productos})


def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect("/")
    else:
        formulario = NewUserForm()
        return render(request,"Reg_user.html", {"form":formulario})
    
def index(request):
    return render(request, 'index.html')


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
    else: 
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



@login_required(login_url='login')
def index(request):
    es_estudiante =request.user.groups.filter(name='Estudiante').exists()
    es_admin = request.user.is_staff
    if es_estudiante or es_admin:
        return render(request, 'index.html',{'user':
request.user, 'es_estudiante': es_estudiante, 'es_admin':
es_admin})

def cerrar_sesion(request):

    logout(request)
    return redirect('login')
