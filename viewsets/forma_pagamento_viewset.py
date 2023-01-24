from financeiro.serializers.forma_pagamento_serializer import FormaPagamentoSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import FormaPagamento


class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated,]
    authentication_classes = (TokenAuthentication,)
   

    filter_backends = [filters.SearchFilter]

    search_fields = []
