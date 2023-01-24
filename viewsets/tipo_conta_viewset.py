from financeiro.serializers.tipo_conta_serializer import TipoContaSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import Rateio


class TipoContaViewSet(viewsets.ModelViewSet):
    queryset = Rateio.objects.all()
    serializer_class = TipoContaSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    

    search_fields = []
