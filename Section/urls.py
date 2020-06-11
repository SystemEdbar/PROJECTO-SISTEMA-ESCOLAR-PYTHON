from django.urls import path
from . import views

urlpatterns =[
    path('<slug:slug>', views.SectionDetailView.as_view(), name='Section')

]
