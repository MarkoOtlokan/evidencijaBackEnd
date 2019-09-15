# string related field -> serializer relations
from .models import *
from rest_framework import serializers


class ProizvodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proizvod
        fields = '__all__'

class UslugaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usluga
        fields = '__all__'


class KlijentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klijent
        fields = '__all__'


class RadnikSerializer(serializers.ModelSerializer):

    class Meta:
        model = Radnik
        fields = '__all__'
