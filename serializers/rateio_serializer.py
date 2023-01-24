
from rest_framework import serializers

from ..models import Rateio


class RateioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rateio
        fields = "__all__"
