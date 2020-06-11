from . import views
from Alumns.views import AlumnListView
from Section.views import SectionListView
from Grade.views import GradeListView
from Inscription.views import InscriptionListView


from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),

    path('listaAlumnos/', AlumnListView.as_view(), name='listAlumns'),
    path('Alumno/', include('Alumns.urls')),
    path('listaGrados/', GradeListView.as_view(), name='listGrade'),
    path('Grado/', include('Grade.urls')),
    path('listaSecciones/', SectionListView.as_view(), name='listSection'),
    path('Seccion/', include('Section.urls')),
    path('listaIncripciones/', InscriptionListView.as_view(), name='listInscription'),
    path('Incripcion/', include('Inscription.urls')),

    path('admin/', admin.site.urls,),
    path('loginUser/', views.loginUser, name="loginUser"),
    path('logoutUser/', views.logoutUser, name="logoutUser"),
    path('registerUser/', views.registerUser, name="registerUser"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
