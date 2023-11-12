from django.shortcuts import render
# Create your views here.
from rest_framework import generics,filters
from .serializers import ImagemSerializer,ImagemCreateSerializer
from .models import Imagem
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


class ListImagem(generics.ListAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['nome','categoria']
    search_fields = ['nome']

class CreateImagemView(CreateAPIView):
    serializer_class = ImagemCreateSerializer
    #permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():

            #serializer.save()

            Response(serializer.data)

        return super().create(request, *args, **kwargs)