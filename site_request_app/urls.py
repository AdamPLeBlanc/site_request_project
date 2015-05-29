from django.conf.urls import patterns, url, include
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    ]
    