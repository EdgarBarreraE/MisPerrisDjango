from django.urls import path
from . import views

urlpatterns = [
    path('Index',views.index,name="index"),
    path('form/',views.form,name="form"),
    path('',views.Inicio,name="Inicio"),
    path('form_rescatado/',views.form_rescatado,name="form_rescatado")

]