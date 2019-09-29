from django.conf.urls import url
from commit import views

urlpatterns = [
    url(r'^commits/(?P<slug>[\w-]+)/$', views.CommitList.as_view(), name='repo-commits'),
    url(r'^user-commits/(?P<slug>[\w-]+)/$', views.UserCommits.as_view(), name='user-commits'),
    url(r'^date-commits/(?P<slug>[\w-]+)/$', views.DateCommits.as_view(), name='date-commits'),
    url(r'^user-date-commits/(?P<slug>[\w-]+)/$', views.UserDateCommits.as_view(), name='user-date-commits')

]