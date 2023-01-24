from financeiro.serializers.conta_nivel2_serializer import ContaNivel2Serializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import ContaNivel2


class ContaNivel2ViewSet(viewsets.ModelViewSet):
    queryset = ContaNivel2.objects.all()
    serializer_class = ContaNivel2Serializer
    filter_backends = [filters.SearchFilter]
    authentication_classes = (TokenAuthentication,)   
    permission_classes = [IsAuthenticated]

 

    search_fields = []
