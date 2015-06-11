from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from .models import Request
from django.utils import timezone

# Create your views here.
    
def index(request):
    rList = Request.objects.order_by('-votes')[:]
    template = loader.get_template('site_request_app/base_index.html')
    context = RequestContext(request,{'sorted_request_list':rList})

    return HttpResponse(template.render(context))
  
def add_request(request):
    template = loader.get_template('site_request_app/base_addrequest.html')
    context = RequestContext(request)
    
    return HttpResponse(template.render(context))
    
def vote(request, request_id):
    r = get_object_or_404(Request,pk=request_id)
    r.votes += 1
    r.save()
    return HttpResponseRedirect(reverse("requests:index"))
    
def process_add_request(request):
    try:
        tmpTitle = request.POST['titleInput']
        tmpDesc = request.POST['descriptionInput']
    except (KeyError, Request.DoesNotExist):
        return render(request, 'site_request_app/base_addrequest.html',{
            'error_message': "You Didnt fill in all the fields",})
    else:
        newRequest = Request(title=tmpTitle,description=tmpDesc,create_date=timezone.now())
        newRequest.save()
        return HttpResponseRedirect(reverse("requests:index"))
        
        
        
        
        