
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Section


class SectionListView(ListView):
    template_name = 'Section/listSection.html'
    queryset = Section.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Secciones'
        context['objects'] = context['object_list']
        return context


class SectionDetailView(DetailView):
    model = Section
    template_name = 'Section/detailSection.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
