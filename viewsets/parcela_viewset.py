from financeiro.serializers.parcela_serializer import ParcelaSerializer
from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import Parcela


class ParcelaViewSet(viewsets.ModelViewSet):
    queryset = Parcela.objects.all()
    serializer_class = ParcelaSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # search_fields = []
