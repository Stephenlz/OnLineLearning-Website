from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url('^list/$', OrgListView.as_view(), name='orgList'),
    url('^userAsk/$', UserAskView.as_view(), name='userAsk'),
    url('^orgHome/(?P<orgName>[\w\W]+)/$', OrgHomeView.as_view(), name='orgHome'),
    url('^orgCourse/(?P<orgName>[\w\W]+)/$', OrgCourseView.as_view(), name='orgCourse'),
    url('^orgDesc/(?P<orgName>[\w\W]+)/$', OrgDescView.as_view(), name='orgDesc'),
    url('^orgTeacher/(?P<orgName>[\w\W]+)/$', OrgTeacherView.as_view(), name='orgTeacher'),
]
