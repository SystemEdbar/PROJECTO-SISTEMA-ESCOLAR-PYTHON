from django.urls import path
from . import views

urlpatterns =[
    path('<slug:slug>', views.GradeDetailView.as_view(), name='Grade')

]
