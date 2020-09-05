from  rest_framework import serializers
from .models import Artigo


class ArtigoSerializer(serializers.Serializer):

    titulo = serializers.CharField(max_length=100)
    autor = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)


    def create(self, validated_data):
        print(validated_data)
        return Artigo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get("title",instance.titulo)
        instance.autor = validated_data.get("autor",instance.autor)
        instance.email = validated_data.get("email",instance.email)

        instance.save()
        return instance


class ArtigoSerializerModel(serializers.ModelSerializer):
    class meta:
        modal = Artigo
        fields = "__all__"