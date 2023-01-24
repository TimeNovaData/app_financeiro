from financeiro.serializers.item_rateio_serializer import ItemRateioSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import ItemRateio


class ItemRateioViewSet(viewsets.ModelViewSet):
    queryset = ItemRateio.objects.all()
    serializer_class = ItemRateioSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

   

    search_fields = []
