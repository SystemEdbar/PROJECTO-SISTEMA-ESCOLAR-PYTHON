from django.contrib import admin
from .models import Grade


class GradeAdmin(admin.ModelAdmin):
    fields = ('nameGrade', 'timeTable')
    list_display = ('__str__', 'slug', 'dateCreate')


admin.site.register(Grade, GradeAdmin)
