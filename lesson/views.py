from rest_framework import generics
from lesson.models import Lesson
from lesson.serializers import LessonSerializer



class LessonCreateAPIView(generics.CreateAPIView): #создание урока
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView): #список всех уроков
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView): #урок по id
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView): #редактирование урока
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView): #удаление урока
    queryset = Lesson.objects.all()
