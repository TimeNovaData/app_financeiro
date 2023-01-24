from financeiro.serializers.banco_serializer import BancoSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from ..models import Banco


class BancoViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
    filter_backends = [filters.SearchFilter]
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

   

    search_fields = []
