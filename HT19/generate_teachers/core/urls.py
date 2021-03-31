from core.views import ContactUsView, ExportStudentsView, \
    GroupCreateView, GroupUpdateView, GroupsView, \
    IndexView, JQApiView, JSApiView, RegistrationView, StudentCreateView, \
    StudentUpdateView, StudentsView, TeacherCreateView, \
    TeacherUpdateView, TeachersView

from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('groups/', GroupsView.as_view(), name='groups'),
    path('group/create', GroupCreateView.as_view(), name='group_create'),
    path('group/update/<int:group_id>/',
         GroupUpdateView.as_view(), name='group_update'),
    path('teachers/', TeachersView.as_view(), name='teachers'),
    path('teachers/create',
         TeacherCreateView.as_view(), name='teachers_create'),
    path('teacher/update/<int:teacher_id>/',
         TeacherUpdateView.as_view(), name='teacher_update'),
    path('students/', StudentsView.as_view(), name='students'),
    path('student/create/',
         StudentCreateView.as_view(), name='student_create'),
    path('student/update/<int:student_id>/',
         StudentUpdateView.as_view(), name='student_update'),
    path('contact_us/', ContactUsView.as_view(), name='contact_us'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path(
        'export/students',
        ExportStudentsView.as_view(),
        name='export_students'
    ),
    path('jsapi/', JSApiView.as_view(), name='jsapi'),
    path('jqapi/', JQApiView.as_view(), name='jqapi'),
]
