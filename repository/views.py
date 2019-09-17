from allauth.socialaccount.models import SocialToken
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from repository.models import Repository
from repository.repositorySerializers import RepositoryReadSerializer, RepositoryWriteSerializer


class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class =RepositoryReadSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method  == "POST":
            return RepositoryWriteSerializer
        else:
            return RepositoryReadSerializer

    def get_serializer_context(self):
        user = {'user':self.request.user}
        return user