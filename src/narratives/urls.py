from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf.urls import include

urlpatterns = [
    url(r'^posts/$', NarrativesList.as_view(), name="narrative_list"),
    #url(r'^posts/post/', include('comments.urls', namespace="comments")),
    url(r'^posts/post/(?P<pk>\d+)/$', Narrative_detail.as_View(), name = "narrative_detail"),
]