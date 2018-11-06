from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('Index',views.index,name="index"),
    path('form/',views.form,name="form"),
    path('',views.Inicio,name="Inicio"),
    path('form_rescatado/', views.form_rescatado, name="form_rescatado"),
    path('form_rescatado/crear_rescatado', views.crear_rescatado, name="crear_rescatado"),
    path('form_rescatado/lista_rescatados', views.lista_rescatados, name="lista_rescatados"),
    path('form_rescatado/editar/<int:id>', views.editar, name="editar"),
    path('form_rescatado/editado/<int:id>', views.editado, name="editado"),
    path('form_rescatado/eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('form_rescatado/buscar/', views.buscar, name="buscar"),
    path('form/crear_persona',views.crear_persona,name="crear_persona"),
    path('Index/administrador',views.administrador,name="administrador")

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)