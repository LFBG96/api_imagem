from django.db import models

# Create your models here.

class Imagem(models.Model):
    nome = models.CharField(max_length=200,null=False,blank=False)
    categoria = models.CharField(max_length=50,null=False,blank=False)
    link = models.URLField(unique=True)
    credito = models.URLField()
