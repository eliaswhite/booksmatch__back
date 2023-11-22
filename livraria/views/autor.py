from livraria.models import Autor
from livraria.serializers import AutorSerializer
from rest_framework.viewsets import ModelViewSet

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer