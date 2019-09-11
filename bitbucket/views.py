import requests
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.providers.bitbucket_oauth2.views import BitbucketOAuth2Adapter
from django.shortcuts import render
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_auth.registration.views import SocialLoginView
from rest_framework.utils import json


class BitBucketLogin(SocialLoginView):
    adapter_class = BitbucketOAuth2Adapter
    callback_url='http://127.0.0.1:4200/'
    client_class=OAuth2Client


