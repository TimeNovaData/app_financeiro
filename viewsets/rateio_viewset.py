from financeiro.serializers.rateio_serializer import RateioSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import Rateio


class RateioViewSet(viewsets.ModelViewSet):
    queryset = Rateio.objects.all()
    serializer_class = RateioSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    

    search_fields = []
