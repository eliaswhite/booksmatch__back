from livraria.models import Livro
from rest_framework.serializers import ModelSerializer, CharField

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

class LivroListSerializer(ModelSerializer):
    capa = CharField(source="capa.url")
    class Meta:
        model = Livro
        fields = ["id", "titulo", "preco", "capa"]