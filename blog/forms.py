# django.form
# import utilities to build forms, e.g. from models
from django.forms import ModelForm
# blog.models
# import our comment model
from blog.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name', 'author_email', 'text')

