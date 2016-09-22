"""GotYou URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main$', views.main),
    url(r'^about$', views.about),
    url(r'^class/os$', views.class_os),
    url(r'^class/db', views.db),
    url(r'^class/db_talk', views.db_talk),
    url(r'^class/os_paper$', views.os_paper),
    url(r'^get_os_result', views.get_os_result),
    url(r'^class/add_db_talk', views.db_talk),
]
