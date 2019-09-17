from rest_framework import serializers

from repository.models import Repository


class RepositoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = "__all__"


class RepositoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        exclude=['user']
        # fields = "__all__"

    def create(self, validated_data):
        user = self.context['user']
        repository = Repository.objects.create(user = user,**validated_data)
        return repository