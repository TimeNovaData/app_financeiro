from financeiro.serializers.caixa_banco_serializer import CaixaBancoSerializer
from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import CaixaBanco


class CaixaBancoViewSet(viewsets.ModelViewSet):
    queryset = CaixaBanco.objects.all()
    serializer_class = CaixaBancoSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    search_fields = []
