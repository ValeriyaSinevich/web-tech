from __future__ import unicode_literals

from django.db import models

class Comment(models.Model):
    #avatar = models.ImageField()
    text = models.TextField()
    narrative = models.ForeignKey('narratives.Narrative', default= 1)
    pub_date = models.DateField(auto_now_add = True)

# Create your models here.
