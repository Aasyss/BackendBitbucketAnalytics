from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from commit.commitSerializer import CommitSerializer
from commit.models import Commit
from repository.models import Repository


class CommitList(generics.ListAPIView):
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

    #
    # def get_serializer_context(self):
    #     user = {'user':self.request.user}
    #     return user