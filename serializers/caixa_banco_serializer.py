from rest_framework import serializers

from ..models import CaixaBanco


class CaixaBancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaixaBanco
        fields = "__all__"
