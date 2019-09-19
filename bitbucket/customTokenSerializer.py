from rest_auth.models import TokenModel
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CustomTokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """
    user = UserDetailsSerializer(many=False, read_only=True)
    class Meta:
        model = TokenModel
        fields = ('key', 'user')