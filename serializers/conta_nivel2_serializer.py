
from rest_framework import serializers

from ..models import ContaNivel2


class ContaNivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ContaNivel2
        fields = "__all__"
