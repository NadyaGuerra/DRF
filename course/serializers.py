from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Course
from lesson.models import Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    count_lessons = SerializerMethodField()  # Количество уроков
    lessons = SerializerMethodField()  # список уроков

    def get_count_lessons(self, course):  # получениe кол-ва уроков
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):  # получениe списка всех уроков
        return [lesson.title for lesson in course.lesson_set.all()]

    class Meta:
        model = Course
        fields = '__all__'
