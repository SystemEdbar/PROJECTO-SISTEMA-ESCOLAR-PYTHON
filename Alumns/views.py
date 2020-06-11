
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView
from .models import Alumn


class AlumnListView(ListView):
    template_name = 'Alumns/listAlumns.html'
    queryset = Alumn.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Alumnos'
        context['objects'] = context['object_list']
        return context


class AlumnDetailView(DetailView):
    model = Alumn
    template_name = 'Alumns/detailAlumn.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
