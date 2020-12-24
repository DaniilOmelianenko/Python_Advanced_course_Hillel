from core.models import Group, Student

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


class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'group': forms.widgets.RadioSelect()
        }


class GroupCreateForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'teacher': forms.widgets.RadioSelect()
        }
