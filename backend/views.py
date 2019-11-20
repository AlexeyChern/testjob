from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class In1View(TemplateView):
    template_name = 'in1.html'

