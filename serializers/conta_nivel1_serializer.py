
from rest_framework import serializers

from ..models import ContaNivel1


class ContaNivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ContaNivel1
        fields = "__all__"
