from django.db import models

# Create your models here.
from repository.models import Repository


class Commit(models.Model):
    message = models.CharField(max_length=200)
    hash = models.CharField(max_length=200,unique=True)
    user = models.CharField(max_length=100)
    date = models.DateTimeField()
    repository = models.ForeignKey(Repository,on_delete=models.CASCADE)

    def __str__(self):
        return  self.user+":"+self.repository.name
