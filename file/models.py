from django.db import models

from repository.models import Repository


class File(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    change_log_url = models.CharField(max_length=500)
    repository = models.ForeignKey(Repository,on_delete=models.CASCADE)

    def __str__(self):
        return  self.name+":"+self.repository.name