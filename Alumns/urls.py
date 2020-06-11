from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.AlumnDetailView.as_view(), name='Alumn')
]
