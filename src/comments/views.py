from django.shortcuts import render
from django.views.generic.detail import DetailView
from models import Comment
from django.shortcuts import render
from annoying.functions import get_object_or_None



class CommentsForNarrative(DetailView):
    model = Comment
    template_name = "comments/comments_for_narrative.html"

    def narrative_detail(request, pk, template_name = "comments/comments_for_narrative.html"):
        comment = get_object_or_None(Comment, narrative=pk)
        return render(request, template_name, {'comment': comment})

# Create your views here.
