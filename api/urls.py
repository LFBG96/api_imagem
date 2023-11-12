from django.urls import path
from .views import ListImagem,CreateImagemView
urlpatterns = [
    path('imagem/',ListImagem.as_view()), 
    path('create/',CreateImagemView.as_view())
]