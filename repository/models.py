from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Repository(models.Model):
    avatar = models.URLField()
    uuid= models.CharField(max_length=50)
    created_on = models.DateField()
    name  = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    updated_on = models.DateField()
    slug = models.SlugField(max_length=50)
    is_private = models.BooleanField()

    def __str__(self):
        return self.name
