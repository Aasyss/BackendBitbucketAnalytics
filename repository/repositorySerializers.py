from rest_framework import serializers

from repository.models import Repository


class RepositoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = "__all__"


class RepositoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = "__all__"