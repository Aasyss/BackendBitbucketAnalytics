import requests
from allauth.socialaccount.models import SocialToken, SocialAccount
from dateutil.parser import parse
from django.contrib.auth.models import User
from django.core.management import BaseCommand


from commit.models import Commit
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
    def update_commits(self):
        repository_list = Repository.objects.all()
        for repository in repository_list:
            user = User.objects.get(id = repository.user_id)
            social_account = SocialAccount.objects.get(user = user)
            social_token = SocialToken.objects.get(account=social_account)

            # requesting commit data from bitbucket api
            r = requests.get(
                "https://bitbucket.org/api/2.0/repositories/" + user.username + "/" + repository.slug + "/commits",
                headers={'Authorization': 'Bearer {}'.format(social_token.token)}, timeout=10)
            if r.status_code == 200:
                data = r.json()
                max_date = Commit.objects.values_list('date', flat=True).filter(repository=repository).latest('date')
                for k in data["values"]:
                    # parsing the string commit date into datetime
                    commit_date = parse(k['date'])

                    # Comparing the date of commits against the maximum date in database
                    if(commit_date>max_date):
                        commit = Commit.objects.create(
                            message = k['message'],
                            hash=k['hash'],
                            date=k['date'],
                            user=k['author']['user']['display_name'],
                            repository=repository)
                        commit.save()

    # handle method calls update_commits() to check the updated commits and if found those commits are stored in database
    def handle(self, *args, **options):
        self.update_commits()

