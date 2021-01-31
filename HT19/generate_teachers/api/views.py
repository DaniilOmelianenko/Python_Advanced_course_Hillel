# from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from api.serializers import GroupSerializer, \
    StudentSerializer, TeacherSerializer

from core.models import Group, Student, Teacher

# from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication,\
    SessionAuthentication
# from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.viewsets import ModelViewSet


# для отключение CSRF ------------------------------------------
class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
# --------------------------------------------------------------


class TeacherViewSet(ModelViewSet):  # full control
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)  # для отключение CSRF # noqa
# class TeacherViewSet(mixins.ListModelMixin,
#                      mixins.RetrieveModelMixin,
#                      GenericViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
