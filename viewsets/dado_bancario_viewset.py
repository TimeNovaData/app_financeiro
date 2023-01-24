from financeiro.serializers.dado_bancario_serializer import DadoBancarioSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import DadoBancario


class DadoBancarioViewSet(viewsets.ModelViewSet):
    queryset = DadoBancario.objects.all()
    serializer_class = DadoBancarioSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    

    search_fields = []
