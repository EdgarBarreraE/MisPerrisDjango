from django.urls import path
from . import views

urlpatterns = [
    path('Index',views.index,name="index"),
    path('form/',views.form,name="form"),
    path('',views.Inicio,name="Inicio"),
    path('form_rescatado/', views.form_rescatado, name="form_rescatado"),
    path('form_rescatado/crear_rescatado', views.crear_rescatado, name="crear_rescatado"),
    path('form_rescatado/lista_rescatados', views.lista_rescatados, name="lista_rescatados"),
    path('form_rescatado/editar/<int:id>', views.editar, name="editar"),
    path('form_rescatado/editado/<int:id>', views.editado, name="editado"),
    path('form_rescatado/eliminar/<int:id>', views.eliminar, name="eliminar")
]