from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index', views.index, name="index"),
    path('form/', views.form, name="form"),
    path('', views.inicio, name="inicio"),
    path('cerrar_sesion', views.cerrar_sesion, name="cerrar_sesion"),
    path('logearse', views.logearse, name="logearse"),
    path('form_rescatado/', views.form_rescatado, name="form_rescatado"),
    path('form_rescatado/crear_rescatado',
         views.crear_rescatado, name="crear_rescatado"),
    path('form_rescatado/lista_rescatados',
         views.lista_rescatados, name="lista_rescatados"),
    path('form_rescatado/editar/<int:id>', views.editar, name="editar"),
    path('form_rescatado/editado/<int:id>', views.editado, name="editado"),
    path('form_rescatado/eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('form_rescatado/buscar/', views.buscar, name="buscar"),
    path('form/crear_persona', views.crear_persona, name="crear_persona"),
    path('password', views.change_password, name='change_password'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
