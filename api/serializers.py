from rest_framework import serializers
from . import models


class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Direction
        fields = ['title', 'position']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    lessons = serializers.PrimaryKeyRelatedField(
        queryset=models.Lesson.objects.all(),
        many=True,
        allow_empty=True,
    )

    class Meta:
        model = models.Course
        fields = ['title', 'position', 'direction', 'lessons']


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    materials = serializers.PrimaryKeyRelatedField(
        queryset=models.LessonMaterial.objects.all(),
        many=True,
        allow_empty=True,
    )

    class Meta:
        model = models.Lesson
        fields = ['title', 'position', 'anons', 'description', 'link_to_video', 'link_to_file', 'materials']


class LessonMaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LessonMaterial
        fields = ['title', 'description', 'image', 'file']
