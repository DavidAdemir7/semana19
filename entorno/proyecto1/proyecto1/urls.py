
from django.contrib import admin
from django.urls import path
from app1 import views as ap1v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ap1v.index,name="home"),
    path('registro/', ap1v.reg_user, name="register"),
    path('login/', ap1v.iniciar_sesion,name="login"),
    path('logout/', ap1v.cerrar_sesion,name="logout"),
    path('proveedores/', ap1v.proveedoresList, name='proveedores-list'),
    path('proveedores/agregar/', ap1v.agregarProveedor, name='agregar-proveedor'),
    path('productos/',ap1v.productosList)
  
    
    
]
