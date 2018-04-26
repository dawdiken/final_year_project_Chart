"""charts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from .views import get_data, ChartUsers, homeView, Data_users, permissionredirect, displayUsers, usertable, displayActiveWork, displayAllWork, worktable, allWorktable, workinfo, \
    about, vote, changeWork, changeWorkInfo

urlpatterns = [
    url(r'^$', homeView, name='homeView'),
    url(r'^permissionredirect$', permissionredirect, name='permissionredirect'),
    url(r'^about$', about, name='about'),
    url(r'^api/chart/users/$', Data_users.as_view(), name='Data_users'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/users_info/$', ChartUsers.as_view()),
    url(r'^admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^api/chart/testing/$', displayUsers.as_view()),
    url(r'^api/chart/table/$', usertable.as_view(), name='usertable'),
    url(r'^api/chart/getworktableActive/$', displayActiveWork.as_view()),
    url(r'^api/chart/getworktableAll/$', displayAllWork.as_view()),
    url(r'^api/chart/changeworkinfo/$', changeWorkInfo.as_view()),
    url(r'^api/chart/worktable/$', worktable.as_view(), name='usertable'),
    url(r'^api/chart/allworktable/$', allWorktable.as_view(), name='Alltable'),
    url(r'^api/chart/changework/$', changeWork.as_view(), name='changeWork'),
    url(r'^api/chart/allworktable/vote$', vote, name='vote'),
    url(r'^api/chart/changework/vote$', vote, name='vote'),
    url(r'^api/chart/workinfo/$', workinfo.as_view(), name='workinfo'),
]

