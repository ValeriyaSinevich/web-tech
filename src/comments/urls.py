from django.conf.urls import url
from django.contrib import admin
from .views import CommentsForNarrative

cfn = CommentsForNarrative()

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', CommentsForNarrative.narrative_detail(cfn, pk=1), name='comments_for_narrative')
]