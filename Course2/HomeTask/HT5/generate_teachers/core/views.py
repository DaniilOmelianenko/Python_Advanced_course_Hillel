from django.db.models import Q
from django.views.generic.base import TemplateView
from core.models import Teacher, Group, Student


# from django.views.generic import CreateView, UpdateView


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
                Q(group__title__contains=self.request.GET['query'])
            )
            context['students'] = students
        return context


class TeachersView(TemplateView):
    template_name = "teachers.html"

    def get_context_data(self, **kwargs):
        teachers = Teacher.objects.all().select_related()

        context = {'greet': "Hello!",
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
