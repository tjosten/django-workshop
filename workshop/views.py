# django.shortcuts
# Required for putting together a response, and other useful tools
from django.shortcuts import render_to_response
# django.http
# http stack, default http response actions
from django.http import Http404, HttpResponseServerError, HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpRequest
# django.template
# functionality required for building templates 
from django.template import RequestContext


########################
# Workshop Core - Views
########################

def welcome_view(request):
    return render_to_response("welcome.html", locals(), context_instance=RequestContext(request))