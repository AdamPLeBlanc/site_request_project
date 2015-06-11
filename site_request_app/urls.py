from django.conf.urls import patterns, url, include
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^add/$',views.add_request,name="addrequest"),
    url(r'^add/newrequest/$',views.process_add_request,name="processaddrequest"),
    url(r'^(?P<request_id>[0-9]+)/vote/$',views.vote,name="vote"),
    ]
    