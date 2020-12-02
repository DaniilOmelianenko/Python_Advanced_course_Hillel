# from abc import ABC
# from django.views.generic import CreateView, FormView, UpdateView
# from django.db.models import Func
# from django.http import Http404
# from django.views.generic import FormView, CreateView
# from django.shortcuts import redirect, get_object_or_404
# from core.forms import GroupForm, StudentForm, TeacherForm
# from django.contrib.auth.models import User
from core.forms import ContactUsForm,\
    RegistrationForm, StudentForm, TeacherForm
from core.models import Group, Student, Teacher
from core.tasks import send_mail_task

from django.contrib.auth import get_user_model
from django.db.models import IntegerField, Q
from django.db.models.aggregates import Avg, Count, Max, Min

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)

        context['inputted_list'] = self.request.GET.get('inputted_list', '')
        context['inputted_string'] = self.request.GET.get('inputted_string', '')

        return context


class StudentsView(TemplateView):
    template_name = "students.html"

    def get_context_data(self, **kwargs):
        students = Student.objects.all().select_related()

        context = {'students': students
                   }

        if 'query' in self.request.GET:
            context['query'] = self.request.GET['query']
            students = students.filter(
                Q(firstname__contains=self.request.GET['query']) |
                Q(group__title__contains=self.request.GET['query']) |
                Q(lastname__contains=self.request.GET['query']) |
                Q(age__contains=self.request.GET['query']) |
                Q(phone__contains=self.request.GET['query'])
            )
            context['students'] = students
        return context


class TeachersView(TemplateView):
    template_name = "teachers.html"

    def get_context_data(self, **kwargs):
        teachers = Teacher.objects.all().select_related()

        context = {
            'teachers': teachers
        }

        if 'query' in self.request.GET:
            context['query'] = self.request.GET['query']
            teachers = teachers.filter(
                Q(first_name__contains=self.request.GET['query']) |
                Q(last_name__contains=self.request.GET['query']) |
                Q(age__contains=self.request.GET['query'])
            )
            context['teachers'] = teachers
        return context


class GroupsView(TemplateView):
    template_name = "groups.html"

    def get_context_data(self, **kwargs):
        # class RoundAge(Func, ABC):
        #     function = 'ROUND'
        #     template = '%(function)s(%(expressions)s)'

        # '''groups = Group.objects.all().select_related().
        # prefetch_related('students')'''
        groups = Group.objects.all().select_related().annotate(
            number_of_students=Count('students'),
            avg_age=Avg('students__age', output_field=IntegerField()),
            # avg_age=(RoundAge(Avg('students__age'))),
            max_age=Max('students__age'),
            min_age=Min('students__age')
        )
        context = {
            'groups': groups
        }
        return context


# 1lvl:
# class StudentCreateView(TemplateView):
#     template_name = 'student_create.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(StudentCreateView, self).get_context_data(**kwargs)
#         context['form'] = StudentCreateForm()
#         return context
#
#     def post(self, request):
#         form = StudentCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#
#         return self.render_to_response({'form': form})


# 2lvl:
# class StudentCreateView(FormView):
#     template_name = 'student_create.html'
#     form_class = StudentCreateForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         form.save()
#         return super(StudentCreateView, self).form_valid(form)
#
#     def form_invalid(self, form):
#         pass


# 3lvl:
class StudentCreateView(CreateView):
    template_name = 'student_create.html'
    success_url = reverse_lazy('students:students')
    model = Student
    fields = '__all__'


class StudentUpdateView(UpdateView):
    template_name = 'student_update.html'
    success_url = reverse_lazy('students:students')
    model = Student
    # fields = '__all__' # если не нужны виджеты
    form_class = StudentForm
    pk_url_kwarg = 'student_id'

    def post(self, request, student_id):
        if 'delete_student' in self.request.POST:
            delete_student = Student.objects.get(pk=student_id)
            delete_student.delete()
            return redirect(reverse_lazy('students:students'))
        return super(StudentUpdateView, self).post(request, student_id)


class GroupCreateView(CreateView):
    template_name = 'group_create.html'
    success_url = reverse_lazy('students:groups')
    model = Group
    fields = '__all__'


class GroupUpdateView(UpdateView):
    template_name = 'group_update.html'
    success_url = reverse_lazy('students:groups')
    model = Group
    fields = '__all__'  # если не нужны виджеты
    # form_class = GroupForm # если нужны виджеты
    pk_url_kwarg = 'group_id'

    def post(self, request, group_id):
        if 'delete_group' in self.request.POST:
            delete_group = Group.objects.get(pk=group_id)
            delete_group.delete()
            return redirect(reverse_lazy('students:groups'))
        return super(GroupUpdateView, self).post(request, group_id)


# --------------------------------------  создание и редактирование учителей
class TeacherCreateView(CreateView):
    template_name = 'teacher_create.html'
    success_url = reverse_lazy('students:teachers')
    model = Teacher
    fields = '__all__'


class TeacherUpdateView(UpdateView):
    template_name = 'teacher_update.html'
    success_url = reverse_lazy('students:teachers')
    model = Teacher
    # fields = '__all__' # если не нужны виджеты
    form_class = TeacherForm
    pk_url_kwarg = 'teacher_id'

    def post(self, request, teacher_id):
        if 'delete_teacher' in self.request.POST:
            delete_teacher = Teacher.objects.get(pk=teacher_id)
            delete_teacher.delete()
            return redirect(reverse_lazy('students:teachers'))
        return super(TeacherUpdateView, self).post(request, teacher_id)
# --------------------------------------


# class StudentUpdateView(TemplateView):  #class StudentUpdateForm(forms.Form)
#     template_name = 'student_update.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # if not Student.objects.filter(
#         #         id=self.kwargs['student_id']
#         # ).exists():
#         #     raise Http404()
#         # student = Student.objects.get(id=self.kwargs['student_id'])
#
#         student = get_object_or_404(Student, id=self.kwargs['student_id'])
#         context['form'] = StudentUpdateForm(initial={
#             'firstname': student.firstname,
#             'lastname': student.lastname,
#             'age': student.age,
#             'group': student.group
#         })
#         return context
#
#     def post(self, request, student_id):
#         form = StudentUpdateForm(data=request.POST)
#         if form.is_valid():
#             form.save(student_id)
#             return redirect('/')
#
#         return self.render_to_response({'form': form})


# class StudentUpdateView(TemplateView):
# '''class StudentUpdateForm(forms.ModelForm):'''
#     template_name = 'student_update.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         student = get_object_or_404(Student, id=self.kwargs['student_id'])
#         context['form'] = StudentUpdateForm(instance=student)
#
#         return context
#
#     def post(self, request, student_id):
#         student = get_object_or_404(Student, id=student_id)
#
#         form = StudentUpdateForm(data=request.POST, instance=student)
#
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#
#         return self.render_to_response({'form': form})


# class StudentUpdateView(FormView):
# '''class StudentUpdateForm(forms.ModelForm):'''
#     template_name = 'student_update.html'
#     form_class = StudentUpdateForm
#     success_url = '/'
#
#     def get_form_kwargs(self):
#         kwargs = super(StudentUpdateView, self).get_form_kwargs()
#         kwargs['instance'] = get_object_or_404(
#             Student,
#             id=self.kwargs['student_id']
#         )
#
#     def form_valid(self, form):
#         form.save()
#         return super(StudentUpdateView, self).form_valid(form)


# class StudentUpdateView(UpdateView):   # исходник апдейта
#     template_name = 'student_update.html'
#     success_url = reverse_lazy('students:students')
#     model = Student
#     # fields = '__all__' # если не нужны виджеты
#     form_class = StudentUpdateForm
#     pk_url_kwarg = 'student_id'


class ContactUsView(FormView):
    template_name = 'contactus.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('students:contact_us')
    fields = '__all__'

    def form_valid(self, form):
        response = super(ContactUsView, self).form_valid(form)
        send_mail_task.delay(
            form.cleaned_data['title'],
            form.cleaned_data['message'],
            form.cleaned_data['email_from']
        )
        return response


class RegistrationView(CreateView):
    model = get_user_model()
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('students:home')


class TeacherAdminView(TemplateView):
    template_name = 'teacher_admin.html'
