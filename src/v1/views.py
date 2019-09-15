from django.http import HttpResponse
from django.shortcuts import render
from django.views import *
from django.views.generic.edit import *
from .models import *
import kronos

from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .pagination import LargeResultsSetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.http import Http404

# import json
# from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.urls  import reverse_lazy
from datetime import datetime



class ProizvodViewSet(viewsets.ModelViewSet):
    serializer_class = ProizvodSerializer
    queryset = serializer_class.Meta.model.objects.all()
#    permission_classes = (IsAuthenticated,)
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^naziv','^napomena','^cena','^created')


class KlijentViewSet(viewsets.ModelViewSet):
    serializer_class = KlijentSerializer
    queryset = serializer_class.Meta.model.objects.all()
#    permission_classes = (IsAuthenticated,)
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^ime','^prezime','^napomena','^created')

class RadnikViewSet(viewsets.ModelViewSet):
    serializer_class = RadnikSerializer
    queryset = serializer_class.Meta.model.objects.all()
#    permission_classes = (IsAuthenticated,)
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^ime','^prezime','^plata','^jmbg','^napomena','^created')


class UslugaViewSet(viewsets.ModelViewSet):
    serializer_class = UslugaSerializer
    queryset = serializer_class.Meta.model.objects.all()
#    permission_classes = (IsAuthenticated,)
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^cena','^created',
                    '^napomena','^klijent',
                    '^radnik','^status')
