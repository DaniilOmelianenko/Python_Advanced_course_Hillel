from core.models import Group, Student, Teacher
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'age', 'group')
    search_fields = ('firstname', 'lastname', 'age')
    list_filter = ('group', )


class TeacherAdmin(UserAdmin):

    list_display = (
        'first_name',
        'last_name',
        'age',
    )

    fieldsets = (
        (
            None,
            {'fields': ('username', 'password')}
        ),
        (
            _('Personal info'),
            {'fields': ('first_name', 'last_name', 'email', 'age')}
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                ),
            }
        ),
        (
            _('Important dates'),
            {'fields': ('last_login', 'date_joined')}
        ),
    )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
