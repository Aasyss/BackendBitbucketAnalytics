
import requests

from allauth.socialaccount.providers.bitbucket_oauth2.views import BitbucketOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from rest_auth.registration.views import SocialLoginView


class BitBucketLogin(SocialLoginView):
    adapter_class = BitbucketOAuth2Adapter
    callback_url='http://127.0.0.1:4200/'
    client_class=OAuth2Client







