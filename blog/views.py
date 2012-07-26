# django.shortcuts
# Required for putting together a response, and other useful tools
from django.shortcuts import render_to_response, get_object_or_404
# django.http
# http stack, default http response actions
from django.http import Http404, HttpResponseServerError, HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpRequest
# django.template
# Functionality required for building templates 
from django.template import RequestContext
# django.db
# e.g. the magic Q thing for creating great queries with the database abstraction layer
from django.db.models import Q
# django.core
# Core packages, e.g. url resolver, Paginator
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# blog.models
# Import our blog's models
from blog.models import *
# blog.forms
# Import our blog's forms
from blog.forms import *
# custom imports
import datetime

############################
# Workshop Blog App - Views
############################

BLOG_ITEMS_PER_PAGE = 3
COMMENTS_PER_PAGE = 3

def list_view(request, page_num=None):

    # We're now going to fetch all available blog entries
    entries_raw = Entry.objects.all().order_by('-pub_date')

    # Initializing the paginator
    paginator = Paginator(entries_raw, BLOG_ITEMS_PER_PAGE)

    # Determining current page
    try:
        entries = paginator.page(page_num)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)

    return render_to_response("blog/list.html", locals(), context_instance=RequestContext(request))

def entry_view(request, url_slug, page_num=None):
    
    # We're trying to fetch the single entry now by the url_slug given
    entry = get_object_or_404(Entry, url_slug=url_slug)


    """
        WORKSHOP NOTE

        This part could be highly optimized. Any ideas? :)
    """

    # Build comment form
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author_name=form.cleaned_data['author_name'],
                author_email=form.cleaned_data['author_email'],
                text=form.cleaned_data['text'],
                pub_date=datetime.datetime.now(),
                entry=entry).save()        
            # clear the comment form
            form = CommentForm()
    else:
        form = CommentForm()

    # Fetching the raw comments for this entry
    comments_raw = Comment.objects.filter(entry=entry).order_by('-pub_date')

    # Initializing the paginator
    paginator = Paginator(comments_raw, COMMENTS_PER_PAGE)

    # Determining current page
    try:
        comments = paginator.page(page_num)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return render_to_response("blog/entry.html", locals(), context_instance=RequestContext(request))

