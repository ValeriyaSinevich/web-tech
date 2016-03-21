from django.shortcuts import render
from django.views.generic.list import ListView
from models import Narrative

# Create your views here.

class NarrativesList(ListView):
    model = Narrative
    template_name = "narratives/narrative_list.html"
