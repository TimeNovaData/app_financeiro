from financeiro.serializers.conta_nivel3_serializer import ContaNivel3Serializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import ContaNivel3


class ContaNivel3ViewSet(viewsets.ModelViewSet):
    queryset = ContaNivel3.objects.all()
    serializer_class = ContaNivel3Serializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    
    search_fields = []
