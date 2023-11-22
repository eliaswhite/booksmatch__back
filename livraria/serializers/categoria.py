from livraria.models import Categoria
from rest_framework.serializers import ModelSerializer

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__" 