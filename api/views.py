from rest_framework import viewsets
from . import models, serializers


class DirectionsViewSet(viewsets.ModelViewSet):
    queryset = models.Direction.objects.all().order_by('-id')
    serializer_class = serializers.DirectionSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all().order_by('-id')
    serializer_class = serializers.CourseSerializer


class LessonsViewSet(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all().order_by('-id')
    serializer_class = serializers.LessonSerializer


class LessonMaterialsViewSet(viewsets.ModelViewSet):
    queryset = models.LessonMaterial.objects.all().order_by('-id')
    serializer_class = serializers.LessonMaterialSerializer
