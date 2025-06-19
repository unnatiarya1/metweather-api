from django.shortcuts import render
from rest_framework import generics
from .models import ClimateData
from .serializers import ClimateDataSerializer

class ClimateDataListView(generics.ListAPIView):
    queryset = ClimateData.objects.all().order_by('-year', '-month')
    serializer_class = ClimateDataSerializer
