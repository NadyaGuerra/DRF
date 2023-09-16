from rest_framework import generics
from lesson.models import Lesson
from lesson.serializers import LessonSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner,IsModerator



class LessonCreateAPIView(generics.CreateAPIView): #создание урока
    serializer_class = LessonSerializer
    permission_classes =[IsModerator]


class LessonListAPIView(generics.ListAPIView): #список всех уроков
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsModerator]


class LessonRetrieveAPIView(generics.RetrieveAPIView): #урок по id
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsModerator]



class LessonUpdateAPIView(generics.UpdateAPIView): #редактирование урока
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsModerator]



class LessonDestroyAPIView(generics.DestroyAPIView): #удаление урока
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsModerator]

