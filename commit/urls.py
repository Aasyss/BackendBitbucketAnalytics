from django.conf.urls import url

from commit import views

urlpatterns = [
    url(r'^commits/(?P<slug>[\w-]+)/$', views.CommitList.as_view(), name='repo-commits')

]