# import requests
# from django.test import Client, TestCase
from core.models import Group, Student, Teacher

from django.test import TestCase
from django.urls import reverse_lazy


class URLAccessTestCase(TestCase):

    # def setUp(self) -> None:  # срабатывает перед каждым тестом
    #     pass
    #
    # def setUpClass(cls):  # срабатывает перед всеми тестами внутри тесткейса
    #     pass
    #
    # def tearDown(self) -> None:  # срабатывает после каждого теста
    #     pass
    #
    # def tearDownClass(cls):  # срабатывает после того как все тесты
    # в классе завершились
    #     pass

    # def setUp(self):
    #     self.client = Client()

    def test_access_home_page(self):
        # response = requests.get('http://127.0.0.1:8000/')  # if server run
        response = self.client.get(reverse_lazy('students:home'))
        # assert response.status_code == 200
        self.assertEqual(response.status_code, 200)

    def test_access_groups_page(self):
        response = self.client.get(reverse_lazy('students:groups'))
        self.assertEqual(response.status_code, 200)

    def test_access_group_create_page(self):
        response = self.client.get(reverse_lazy('students:group_create'))
        self.assertEqual(response.status_code, 200)

    def test_access_group_update_page(self):
        teacher = Teacher.objects.create(
            first_name='TestTeacher'
        )
        group = Group.objects.create(
            title='TestGroup',
            teacher=teacher
        )
        response = self.client.get(
            reverse_lazy('students:group_update', args=[group.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_access_teachers_page(self):
        response = self.client.get(reverse_lazy('students:teachers'))
        self.assertEqual(response.status_code, 200)

    def test_access_teachers_create_page(self):
        response = self.client.get(reverse_lazy('students:teachers_create'))
        self.assertEqual(response.status_code, 200)

    def test_access_teacher_update_page(self):
        teacher = Teacher.objects.create(
            first_name='TestTeacher'
        )
        response = self.client.get(
            reverse_lazy('students:teacher_update', args=[teacher.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_access_students_page(self):
        response = self.client.get(reverse_lazy('students:students'))
        self.assertEqual(response.status_code, 200)

    def test_access_student_create_page(self):
        response = self.client.get(reverse_lazy('students:student_create'))
        self.assertEqual(response.status_code, 200)

    def test_access_student_update_page(self):
        teacher = Teacher.objects.create(
            first_name='TestTeacher'
        )
        group = Group.objects.create(
            title='TestGroup',
            teacher=teacher
        )
        student = Student.objects.create(
            group=group
        )
        response = self.client.get(
            reverse_lazy('students:student_update', args=[student.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_access_contact_us_page(self):
        response = self.client.get(reverse_lazy('students:contact_us'))
        self.assertEqual(response.status_code, 200)

    def test_access_registration_page(self):
        response = self.client.get(reverse_lazy('students:registration'))
        self.assertEqual(response.status_code, 200)


class CountOnPagesTestCase(TestCase):

    def test_group_count(self):
        teacher = Teacher.objects.create(
            first_name='TestTeacher'
        )
        test_groups_count = 10

        for group in range(test_groups_count):
            Group.objects.create(
                title='TestGroup',
                teacher=teacher
            )

        response = self.client.get(reverse_lazy('students:teachers'))
        self.assertEqual(
            response.context['teachers'].last().teacher_groups.count(),
            test_groups_count
        )

    def test_student_count(self):
        teacher = Teacher.objects.create(
            first_name='TestTeacher'
        )
        group = Group.objects.create(
            title='TestGroup',
            teacher=teacher
        )
        test_students_count = 10

        for student in range(test_students_count):
            Student.objects.create(
                group=group
            )
        response = self.client.get(reverse_lazy('students:teachers'))
        self.assertEqual(
            response.context['teachers'].last().teacher_groups.last().
            students.count(),
            test_students_count
        )
