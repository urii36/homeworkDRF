from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', null=True)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', null=True)
    url = models.URLField(verbose_name='ссылка на видео')

    def __str__(self):
        return f'{self.title}'
