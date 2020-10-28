# from abc import ABC
# from core.forms import StudentCreateForm
# from django.db.models import Func
# from django.shortcuts import redirect
# from django.views.generic import FormView, CreateView
from core.models import Group, Student, Teacher

from django.db.models import IntegerField, Q
from django.db.models.aggregates import Avg, Count, Max, Min
from django.views.generic import CreateView
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

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
                Q(age__contains=self.request.GET['query'])
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
                Q(firstname__contains=self.request.GET['query']) |
                Q(lastname__contains=self.request.GET['query']) |
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
    success_url = '/'
    model = Student
    fields = '__all__'


class GroupCreateView(CreateView):
    template_name = 'group_create.html'
    success_url = '/'
    model = Group
    fields = '__all__'
