from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from file.fileSerializer import FileSerializer
from file.models import File
from repository.models import Repository
from rest_framework.response import Response
from django.core import serializers


class FileList(ListAPIView):
    queryset = File.objects.all()
    serializer_class =FileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs['slug']
        return File.objects.raw("select * from file_file f join repository_repository r on f.repository_id=r.id where r.slug='%s'"%slug)

    def List(self):
        queryset = self.get_queryset()
        serializer = FileSerializer(queryset, many=True)
        return Response(serializer.data)

