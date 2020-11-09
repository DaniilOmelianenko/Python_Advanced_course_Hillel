from core.models import Group, Student, Teacher
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'age', 'group')
    search_fields = ('firstname', 'lastname', 'age')
    list_filter = ('group', )


class TeacherAdmin(UserAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
