from rest_framework import serializers
from .models import Rescatado


class RescatadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Rescatado
        fields=('url','foto','nombre','raza','descripcion','estado')

