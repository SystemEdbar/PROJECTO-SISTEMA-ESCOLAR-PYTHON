from django.contrib import admin
from .models import Inscription


class InscriptionAdmin(admin.ModelAdmin):
    fields = ('numberInscription','nameAlumn', 'nameGrade', 'nameSection')
    list_display = ('__str__', 'slug', 'dateCreate')


admin.site.register(Inscription, InscriptionAdmin)
