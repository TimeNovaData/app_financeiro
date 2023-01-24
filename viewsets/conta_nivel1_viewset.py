from financeiro.serializers.conta_nivel1_serializer import ContaNivel1Serializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import ContaNivel1


class ContaNivel1ViewSet(viewsets.ModelViewSet):
    queryset = ContaNivel1.objects.all()
    serializer_class = ContaNivel1Serializer
    filter_backends = [filters.SearchFilter]
    filter_backends = [filters.SearchFilter]
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    

    

    search_fields = []
