from financeiro.serializers.conta_nivel4_serializer import ContaNivel4Serializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import ContaNivel4


class ContaNivel4ViewSet(viewsets.ModelViewSet):
    queryset = ContaNivel4.objects.all()
    serializer_class = ContaNivel4Serializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    

    search_fields = []
