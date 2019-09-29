from django.db.models import Count
from django.http import JsonResponse
from rest_framework import serializers

from commit.models import Commit


class CommitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commit
        fields = "__all__"
#
# class CommitReadSerializer(serializers.ModelSerializer):
#     user_commit_count = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Commit
#         # fields="__all__"
#         fields = ['user_commit_count']
#
#     def get_user_commit_count(self,obj):
#         # repository = self.context['repository']
#         # commits = Commit.objects.filter(repository = repository).values('user').annotate(Count('user'))
#         return obj
