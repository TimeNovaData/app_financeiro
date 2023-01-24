
from rest_framework import serializers

from ..models import TipoDocumentoFinanceiro


class TipoDocumentoFinanceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoFinanceiro
        fields = "__all__"
