from django.shortcuts import render
from django.views.generic import TemplateView


class indexView(TemplateView):
    template_name = 'enigma/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio - Enigma'
        context['version'] = '1.0.1'
        return context



