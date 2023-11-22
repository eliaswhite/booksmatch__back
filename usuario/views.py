from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate, get_user_model
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from django.db.models import Q

from .models import Usuario
from .serializers import UsuarioSerializer

User = get_user_model()

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    print(username, password)

    if username is not None and password is not None:
        try:
            user = User.objects.get(Q(username=username))
        except User.DoesNotExist:
            user = None
            
    else:
        return Response(
            {"message": "Credenciais inválidas!"}, status=status.HTTP_400_BAD_REQUEST
        )

    print(user)

    if user is not None:

        response_data = {
            "username": user.username,
            "email": user.email,
            "id": user.id,
            "message": "Login realizado com sucesso!"
            # Adicione outros campos do usuário que você deseja retornar
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response(
            {"message": "Credenciais inválidas!"}, status=status.HTTP_400_BAD_REQUEST
        )
