from core.models import Group, Student, Teacher

from django.contrib import admin


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'age', 'group')
    search_fields = ('firstname', 'lastname', 'age')
    list_filter = ('group', )


admin.site.register(Teacher)
admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
