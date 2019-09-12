from allauth.socialaccount.models import SocialToken
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from repository.models import Repository
from repository.repositorySerializers import RepositoryReadSerializer


class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class =RepositoryReadSerializer
    permission_classes = [IsAuthenticated]