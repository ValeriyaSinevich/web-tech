from django.shortcuts import render
from django.views.generic.list import ListView
from models import Narrative
from comments.models import Comment
from django.views.generic.detail import DetailView
from django.shortcuts import render
from annoying.functions import get_object_or_None

# Create your views here.

class NarrativesList(ListView):
    model = Narrative
    template_name = "narratives/narrative_list.html"

class Narrative_detail(DetailView):
    model = Comment
    template_name = "narratives/comments_for_narrative.html"




