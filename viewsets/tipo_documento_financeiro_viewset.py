from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from financeiro.serializers.tipo_documento_financeiro_serializer import (
    TipoDocumentoFinanceiroSerializer,
)

from ..models import TipoDocumentoFinanceiro


class TipoDocumentoFinanceiroViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumentoFinanceiro.objects.all()
    serializer_class = TipoDocumentoFinanceiroSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    search_fields = []
