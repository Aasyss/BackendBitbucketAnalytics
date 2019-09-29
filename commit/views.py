from django.db.models import Count
from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from commit.commitSerializer import CommitSerializer
from commit.models import Commit
from repository.models import Repository


class CommitList(ListAPIView):
    queryset = Commit.objects.all()
    serializer_class =CommitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Commit.objects.raw("select * from commit_commit c join repository_repository r on c.repository_id=r.id where r.slug='%s'"%slug)

    def List(self):
        queryset = self.get_queryset()
        serializer = CommitSerializer(queryset, many=True)
        return Response(serializer.data)

'''
    APIView for getting the commit count by users in a repository
    select data is used for formatting the date in YYYY-MM-DD format
'''
class UserCommits(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,slug):
        repository= Repository.objects.get(slug=slug)
        #  SQL equivalent => select user,count(user) as count from commit_commit where repository_id=16 group by user;
        user_commit_count = Commit.objects.values('user').annotate(commit_count=Count('user')).filter(repository=repository)

        return Response(user_commit_count)


'''
    APIView for getting the commit count by a specific date
    select data is used for formatting the date in YYYY-MM-DD format
'''
class DateCommits(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,slug):
        repository = Repository.objects.get(slug=slug)
        select_data = {"date": """strftime('%%Y-%%m-%%d', date)"""}
        # SQL equivalent => select strftime('%Y-%m-%d',date) as date,count(strftime('%Y-%m-%d',date)) as count from commit_commit where repository_id=19 group by strftime('%Y-%m-%d',date);
        date_commit_count = Commit.objects.extra(select=select_data).values('date').annotate(Count('date')).filter(repository=repository)

        return Response(date_commit_count)

'''
    APIView for getting the user's commit count in a specific date
    select data is used for formatting the date in YYYY-MM-DD format
'''
class UserDateCommits(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,slug):
        repository = Repository.objects.get(slug=slug)
        user_date_commit_counts = {}
        select_data = {"date": """strftime('%%Y-%%m-%%d', date)"""}
        # SQL eqivalent => select user,count(user) as count,strftime('%Y-%m-%d',date) as date from commit_commit where repository_id=16 group by strftime('%Y-%m-%d',date);
        date_commit_count = Commit.objects.extra(select=select_data).values('date','user').annotate(Count('user')).filter(repository=repository).order_by('date')
        user_list = list(set(Commit.objects.values_list('user',flat=True).filter(repository=repository)))
        for commit in date_commit_count:
            if not commit['date'] in user_date_commit_counts.keys():
                user_date_commit_counts[commit['date']] = [{commit['user']:commit['user__count']}]
            else:
                user_date_commit_counts[commit['date']].append({commit['user']:commit['user__count']})

                        # user_date_commit_counts[commit['date']].append({'user':commit['user'] , 'count':commit['user__count']})
        user_counter = 0

        for key in user_date_commit_counts:
            dict = set().union(*(d.keys() for d in user_date_commit_counts[key]))
            for user in user_list:
                if not user in dict:
                    user_date_commit_counts[key].append({user: 0})

        return Response(user_date_commit_counts)
