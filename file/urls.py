from django.conf.urls import url
from file import views

urlpatterns = [
    url(r'^files/(?P<slug>[\w-]+)/$', views.FileList.as_view(), name='repo-files'),

]