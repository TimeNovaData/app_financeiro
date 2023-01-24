from financeiro.serializers.lancamento_financeiro_serializer import LancamentoFinanceiroSerializer
from rest_framework import filters, viewsets, views
from rest_framework.permissions import IsAuthenticated
from ..models import LancamentoFinanceiro
from rest_framework.authentication import TokenAuthentication


class LancamentoFinanceiroViewSet(viewsets.ModelViewSet):
    queryset = LancamentoFinanceiro.objects.all()
    serializer_class = LancamentoFinanceiroSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    search_fields = []
