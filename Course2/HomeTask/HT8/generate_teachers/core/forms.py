# from core.fields import PhoneField
from core.models import Group, Student, Teacher

from django import forms


# class StudentCreateForm(forms.Form):
#     firstname = forms.CharField()
#     lastname = forms.CharField()
#     age = forms.IntegerField()
#     group = forms.ModelChoiceField(
#         queryset=Group.objects.all(),
#         widget=forms.widgets.RadioSelect()
#     )
#
#     def save(self):
#         return Student.objects.create(**self.cleaned_data)


class StudentForm(forms.ModelForm):

    # phone = PhoneField()

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'group': forms.widgets.RadioSelect()
        }

    # def save(self, commit=True):
    #     print(self.cleaned_data.pop('phone'))
    #     return super(StudentForm, self).save(commit)


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'teacher': forms.widgets.RadioSelect()
        }


# class StudentUpdateForm(forms.Form):
#     firstname = forms.CharField()
#     lastname = forms.CharField()
#     age = forms.IntegerField()
#     group = forms.ModelChoiceField(
#         queryset=Group.objects.all(),
#         widget=forms.widgets.RadioSelect()
#     )
#
#     def save(self, student_id=None):
#         return Student.objects.update_or_create(id=student_id,
#         defaults=self.cleaned_data)[0]
#
#         # return Student.objects.filter(id=student_id). \
#         update(**self.cleaned_date) - если только апдейт


# class StudentUpdateForm(forms.ModelForm):
#
#     class Meta:
#         model = Student
#         fields = '__all__'
#         widgets = {
#             'group': forms.widgets.RadioSelect()
#         }


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'
