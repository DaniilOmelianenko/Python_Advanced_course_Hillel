from core.models import Group, Student, Teacher

from rest_framework import serializers


# class TeacherSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     username = serializers.CharField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     age = serializers.CharField()

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'age',
        )


# class GroupSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     teacher = TeacherSerializer()

class GroupSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Group
        fields = '__all__'


# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField(source='firstname')
#     last_name = serializers.CharField(source='lastname')
#     age = serializers.CharField()  # если сорс такойже, его писать не нужно
#     group = GroupSerializer()
#     phone = serializers.CharField()
#     experience = serializers.SerializerMethodField()
#
#     def get_experience(self, object):
#         return object.get_experience_display()

class StudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    experience = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'

    def get_experience(self, obj):
        return obj.get_experience_display()

# Для many 2 many филдов:
    # # tags = TagsSerializer(many=True)
    # tags = serializers.SerializerMethodField()
    #
    # def get_tags(self, obj):
    #     return [x.name for x in obj.tags.all()]
