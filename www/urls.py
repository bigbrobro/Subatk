"""www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Subatk.views import Index,Add,TaskDel,TaskShow,Tasktext,Taskopen
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/',Index.as_view()),
    url(r'^add/',Add.as_view()),
    url(r'^task/del/(?P<taskid>\d+)/$', TaskDel.as_view()),
    url(r'^task/show/(?P<taskid>\d+)/$', TaskShow.as_view()),
    url(r'^task/cmd/(?P<taskid>\d+)/$', Tasktext.as_view()),
    url(r'^task/open/(?P<taskid>\d+)/$', Taskopen.as_view()),
]
