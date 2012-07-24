from django.contrib import admin
from blog.models import *
# settings
# Import values from settings
from workshop.settings import STATIC_URL

class TinyMceMedia:
    js = (
        STATIC_URL + 'tiny_mce/tiny_mce.js',
        STATIC_URL + 'js/textareas.js',
    )

class EntryAdmin(admin.ModelAdmin):
    # Set up the url_slug field to be autopopulated
    prepopulated_fields = {'url_slug':('title',),}
    Media = TinyMceMedia

admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment)