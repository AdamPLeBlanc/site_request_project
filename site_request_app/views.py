from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

# Create your views here.


def index(request):
    return render_to_response('site_request_app/index.html')