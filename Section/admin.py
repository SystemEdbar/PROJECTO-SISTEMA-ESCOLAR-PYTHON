from django.contrib import admin
from .models import Section


class SectionAdmin(admin.ModelAdmin):
    fields = ('nameSection', 'workingDay')
    list_display = ('__str__', 'slug', 'dateCreate')


admin.site.register(Section, SectionAdmin)
