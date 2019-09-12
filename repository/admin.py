from django.contrib import admin

# Register your models here.
from repository.models import Repository

admin.site.register(Repository)
