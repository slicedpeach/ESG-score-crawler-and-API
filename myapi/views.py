from django.shortcuts import render
from rest_framework import viewsets


import csv

from .serializers import CompanySerializer

from .models import Company




class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

   