
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Inscription


class InscriptionListView(ListView):
    template_name = 'Inscription/listInscription.html'
    queryset = Inscription.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Grados'
        context['objects'] = context['object_list']
        return context


class InscriptionDetailView(DetailView):
    model = Inscription
    template_name = 'Inscription/detailInscription.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
