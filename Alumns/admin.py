from django.contrib import admin
from .models import Alumn


class AlumnAdmin(admin.ModelAdmin):
    fields = ('carnetAlumn', 'nameAlumn', 'surnameAlumn', 'directionAlumn','imageAlumn')
    list_display = ('__str__', 'carnetAlumn', 'dateCreate')


admin.site.register(Alumn, AlumnAdmin)
