from allauth.socialaccount.providers.bitbucket_oauth2.views import BitbucketOAuth2Adapter
from django.shortcuts import render

# Create your views here.
from rest_auth.registration.views import SocialLoginView


class BitBucketLogin(SocialLoginView):
    adapter_class = BitbucketOAuth2Adapter