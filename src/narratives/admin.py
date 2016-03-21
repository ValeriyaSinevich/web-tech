from django.contrib import admin

from .models import Narrative
from .comments.models import Comment

admin.site.register(Narrative)
admin.register(Comment)

# Register your models here.
