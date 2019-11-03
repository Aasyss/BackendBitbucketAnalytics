import requests
from allauth.socialaccount.models import SocialToken, SocialAccount
from dateutil.parser import parse
from django.contrib.auth.models import User
from django.core.management import BaseCommand


from commit.models import Commit
from file.models import File
from repository.models import Repository

class Command(BaseCommand):
    '''
    - Method to update commits
    - Iterates over all the imported repository of the user
    - Requests all the commits in the repository to bitbucket API by providing bitbucket username, repository slug in the url
    - Bitbucket access token is also sent in header to ensure the authenticity of the user
    - To store the commits retrieved for a repository
    - Commit is added if the commit date is greater than maximum date of commits in that repository
    '''
    def update_files(self):
        repository_list = Repository.objects.all()
        File.objects.all().delete()

        for repository in repository_list:
            user = User.objects.get(id = repository.user_id)
            social_account = SocialAccount.objects.get(user = user)
            social_token = SocialToken.objects.get(account=social_account)

            # requesting commit data from bitbucket api
            r = requests.get(
                "https://bitbucket.org/api/2.0/repositories/" + user.username + "/" + repository.slug + "/src",
                headers={'Authorization': 'Bearer {}'.format(social_token.token)}, timeout=10)
            if r.status_code == 200:
                data = r.json()
                print("repo:",repository.name)
                for k in data["values"]:
                    file = File.objects.create(
                        name = k['path'],
                        type = k['mimetype'] if k['mimetype']!=None else "unknown",
                        change_log_url=k['links']['history']['href'],
                        repository=repository)
                    file.save()

    # handle method calls update_commits() to check the updated commits and if found those commits are stored in database
    def handle(self, *args, **options):
        self.update_files()

