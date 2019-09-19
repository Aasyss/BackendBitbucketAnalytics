import requests
from allauth.socialaccount.models import SocialAccount, SocialToken
from dateutil.parser import parse
from rest_framework import serializers

from commit.models import Commit
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
        # inserting the commits while importing the repository
        social_account = SocialAccount.objects.get(user=user)
        social_token = SocialToken.objects.get(account=social_account)

        r = requests.get(
            "https://bitbucket.org/api/2.0/repositories/" + user.username + "/" + repository.slug + "/commits",
            headers={'Authorization': 'Bearer {}'.format(social_token.token)}, timeout=10)
        if r.status_code == 200:
            data = r.json()

            for k in data["values"]:
                commit = Commit.objects.create(
                    message=k['message'],
                    hash=k['hash'],
                    date=k['date'],
                    user=k['author']['user']['display_name'],
                    repository=repository)
                commit.save()

        return repository