from rest_framework import serializers

from ..models import Parcela


class ParcelaSerializer(serializers.ModelSerializer):
    valor_efetivo = serializers.ReadOnlyField()

    class Meta:
        model = Parcela
        fields = "__all__"
