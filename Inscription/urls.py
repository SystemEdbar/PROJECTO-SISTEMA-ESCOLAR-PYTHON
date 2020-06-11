from django.urls import path
from . import views

urlpatterns =[
    path('<slug:slug>', views.InscriptionDetailView.as_view(), name='Inscription')

]
