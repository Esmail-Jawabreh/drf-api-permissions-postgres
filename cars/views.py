from django.shortcuts import render
from rest_framework import generics
from .models import Cars
from .serializers import CarsSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly

# Create your views here.


# ListAPIView
class CarsList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = [IsAuthenticated]


# RetrieveAPIView RetrieveUpdateAPIView
class CarsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = [IsOwnerOrReadOnly]
