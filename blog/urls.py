from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # The list_view, our Homepage with all our blog entries listed, including a page option behind it
    url(r'^$', 'blog.views.list_view', name='blog-home'),
    url(r'^(?P<page_num>(\d+))/$', 'blog.views.list_view', name='blog-home'),

    # The entry_view, displaying a single Entry with comments etc.
    url(r'^(?P<url_slug>([-\w]+))/$', 'blog.views.entry_view', name='blog-entry'),
    url(r'^(?P<url_slug>([-\w]+))/(?P<page_num>(\d+))/$', 'blog.views.entry_view', name='blog-entry'),
)


