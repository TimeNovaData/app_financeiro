
from rest_framework import serializers

from ..models import ItemRateio


class ItemRateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRateio
        fields = "__all__"
