
from rest_framework import serializers

from ..models import ContaNivel3


class ContaNivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = ContaNivel3
        fields = "__all__"
