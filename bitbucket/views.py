import time

import requests
from allauth.socialaccount.models import SocialAccount, SocialToken
from allauth.socialaccount.providers.bitbucket_oauth2.views import BitbucketOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class BitBucketLogin(SocialLoginView):
    adapter_class = BitbucketOAuth2Adapter
    callback_url='http://127.0.0.1:4200/'
    client_class=OAuth2Client

'''
 - get method for /all-repository endpoint
 - provides all the repositories of logged in user
 - Access token is passed in the header of request to get the private repositories of  user
'''
MAX_RETRIES = 5
class AllRepositoriesApi(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            token = request.auth.pk
            token_user = Token.objects.select_related('user').get(key = token)
            username = token_user.user.username
            account = SocialAccount.objects.get(user_id = token_user.user_id)
            access_token= SocialToken.objects.get(account=account)
            attempt_num = 0  # keep track of how many times we've retried
            while attempt_num < MAX_RETRIES:
                r = requests.get("https://bitbucket.org/api/2.0/repositories/"+username,headers={'Authorization': 'Bearer {}'.format(access_token)}, timeout=10)
                if r.status_code == 200:
                    data = r.json()
                    return Response(data, status=status.HTTP_200_OK)
                else:
                    attempt_num += 1
                    time.sleep(5)  # Wait for 5 seconds before re-trying
            return Response({"error": "Request failed"}, status=r.status_code)
        else:
            return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)


'''
 - get method for /repository/<slug> endpoint
 - provides the detailed data of repository selected by logged in user
 - Access token is passed in the header of request to get private repository data 
'''
class getRepositoryDetail(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            token = request.auth.pk
            token_user = Token.objects.select_related('user').get(key = token)
            username = token_user.user.username
            account = SocialAccount.objects.get(user_id = token_user.user_id)
            access_token= SocialToken.objects.get(account=account)
            repo_slug = self.kwargs['slug']
            attempt_num = 0  # keep track of how many times we've retried
            while attempt_num < MAX_RETRIES:
                r = requests.get("https://bitbucket.org/api/2.0/repositories/"+username+"/"+repo_slug,headers={'Authorization': 'Bearer {}'.format(access_token)}, timeout=10)
                if r.status_code == 200:
                    data = r.json()
                    return Response(data, status=status.HTTP_200_OK)
                else:
                    attempt_num += 1
                    # You can probably use a logger to log the error here
                    time.sleep(5)  # Wait for 5 seconds before re-trying
            return Response({"error": "Request failed"}, status=r.status_code)
        else:
            return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)







