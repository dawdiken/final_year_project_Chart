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

from .views import Data_home, get_data, ChartData, homeView

urlpatterns = [
    url(r'^$', homeView, name='homeView'),
    url(r'^api/chart/this/$', Data_home.as_view(), name='Data_home'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^admin/', admin.site.urls),
    # url(r'^setcol', set_color , name='set_col'),
    # url(r'^showcol', show_color , name='set_col'),
    url('accounts/', include('django.contrib.auth.urls')),
]

