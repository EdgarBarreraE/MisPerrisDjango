from rest_framework import serializers
from .models import Rescatado
from .models import Usuario

class RescatadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Rescatado
        fields=('url','id','foto','nombre','raza','descripcion','estado')


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Usuario
        fields=('url','id','nombres','apellidos','rut','email','fechaNacimiento','telefono','tipoCasa','region','comuna')

