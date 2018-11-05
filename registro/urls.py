from django.urls import path
from . import views

"""
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_complete, password_reset_confirm
"""

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="index"),
    path('form/',views.form,name="form"),
    path('login',views.inicio,name="inicio"),
    path('cerrar_sesion',views.cerrar_sesion,name="cerrar_sesion"),
    path('logearse',views.logearse,name="logearse"),
    path('form_rescatado/', views.form_rescatado, name="form_rescatado"),
    path('form_rescatado/crear_rescatado', views.crear_rescatado, name="crear_rescatado"),
    path('form_rescatado/lista_rescatados', views.lista_rescatados, name="lista_rescatados"),
    path('form_rescatado/editar/<int:id>', views.editar, name="editar"),
    path('form_rescatado/editado/<int:id>', views.editado, name="editado"),
    path('form_rescatado/eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('form_rescatado/buscar/', views.buscar, name="buscar"),
    path('form/crear_persona',views.crear_persona,name="crear_persona")

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)