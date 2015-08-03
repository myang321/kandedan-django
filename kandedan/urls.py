__author__ = 'Steve'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^main$', views.main, name='main'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^add', views.add, name='add'),
]
