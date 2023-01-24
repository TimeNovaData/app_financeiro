
from rest_framework import serializers

from ..models import ContaNivel4


class ContaNivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = ContaNivel4
        fields = "__all__"
