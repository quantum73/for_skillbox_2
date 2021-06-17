from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models


class Direction(models.Model):
    title = models.CharField(max_length=128, verbose_name='название')
    position = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='позиция',
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'направления'

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=128, verbose_name='название')
    position = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='позиция',
        validators=[MinValueValidator(0)]
    )
    direction = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='направление',
        validators=[MinValueValidator(0)]
    )
    lessons = ArrayField(models.IntegerField(), default=list, verbose_name='уроки')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=128, verbose_name='название')
    position = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='позиция',
        validators=[MinValueValidator(0)]
    )
    anons = models.TextField(null=True, blank=True, verbose_name='анонс')
    description = models.TextField(null=True, blank=True, verbose_name='описание')
    link_to_video = models.URLField(null=True, blank=True, verbose_name='ссылка к видео')
    link_to_file = models.URLField(null=True, blank=True, verbose_name='ссылка к файлу')
    materials = ArrayField(models.IntegerField(), default=list, verbose_name='материалы')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.title


class LessonMaterial(models.Model):
    title = models.CharField(max_length=128, verbose_name='название')
    description = models.TextField(null=True, blank=True, verbose_name='описание')
    image = models.URLField(null=True, blank=True, verbose_name='ссылка к картинке')
    file = models.URLField(null=True, blank=True, verbose_name='ссылка к файлу')

    class Meta:
        verbose_name = 'материал к уроку'
        verbose_name_plural = 'материалы к уроку'

    def __str__(self):
        return self.title
