 # coding=utf8

# django.db
# Import basic models and field definitions
from django.db import models
# django.contrib.auth.models
# Import django user model
from django.contrib.auth.models import User
# datetime
# Python datetime
from datetime import datetime
# workshop.settings
# import our settings
from workshop.settings import MEDIA_ROOT

class Entry(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, help_text="Titel des Blog-Eintrags")
    text = models.TextField(null=False, blank=False, help_text="Der Blog-Eintrag")
    pub_date = models.DateTimeField(default=datetime.now(), help_text="Datum und Uhrzeit")
    author = models.ForeignKey(User, null=False, blank=False, help_text="Autor")
    url_slug = models.SlugField(max_length=255, null=False, blank=False, unique=True, help_text="URL-Slug für diesen Eintrag")
    image = models.ImageField(upload_to="keyvisuals/", help_text="Keyvisual-Bild für diesen Artikel")

    def __unicode__(self):
        return "%s (von %s)" % (self.title, self.author)

    class Meta:
        verbose_name = 'Eintrag'
        verbose_name_plural = 'Einträge'

class Comment(models.Model):
    entry = models.ForeignKey(Entry, null=False, blank=False)
    author_name = models.CharField(max_length=100, null=False, blank=False, help_text="Name des Autors", verbose_name="Name")
    author_email = models.EmailField(null=False, blank=False, help_text="E-Mail Adresse des Autors", verbose_name="E-Mail Adresse")
    pub_date = models.DateTimeField(default=datetime.now(), help_text="Datum und Uhrzeit")
    text = models.TextField(null=False, blank=False, max_length=500, help_text="Der Kommentar", verbose_name="Kommentar")

    def __unicode__(self):
        return "%s zu %s" % (self.author_name, self.entry)

    class Meta:
        verbose_name = 'Kommentar'
        verbose_name_plural = 'Kommentare'