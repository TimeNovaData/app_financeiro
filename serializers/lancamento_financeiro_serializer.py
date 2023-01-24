
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from ..models import LancamentoFinanceiro


class LancamentoFinanceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = LancamentoFinanceiro

        fields = "__all__"
