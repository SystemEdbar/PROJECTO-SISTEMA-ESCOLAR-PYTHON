
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Grade


class GradeListView(ListView):
    template_name = 'Grade/listGrade.html'
    queryset = Grade.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Grados'
        context['objects'] = context['object_list']
        return context


class GradeDetailView(DetailView):
    model = Grade
    template_name = 'Grade/detailGrade.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
