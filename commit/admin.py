from django.contrib import admin

# Register your models here.
from commit.models import Commit

admin.site.register(Commit)