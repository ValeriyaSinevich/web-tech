from __future__ import unicode_literals

from django.db import models

class Narrative(models.Model):
    #avatar = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add = True)

# Create your models here.
