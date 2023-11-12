from rest_framework import serializers
from .models import Imagem

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'

class ImagemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ('nome','categoria','link','credito')

    def create(self, validated_data):
        nome = validated_data.get("nome")
        categoria = validated_data.get("categoria")
        link = validated_data.get("link")
        credito = validated_data.get("credito")

        imagem = Imagem.objects.create(
            nome=nome,
            categoria=categoria,
            link=link,
            credito=credito
        )
        imagem.save()

        return imagem