from livraria.models.livro import Livro
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from livraria.serializers import LivroSerializer, LivroDetailSerializer, LivroListSerializer

from django_filters.rest_framework import DjangoFilterBackend

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categoria__descricao"]

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer