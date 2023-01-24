from rest_framework import serializers

from ..models import DadoBancario


class DadoBancarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadoBancario
        fields = "__all__"
