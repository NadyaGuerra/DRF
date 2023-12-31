from django.db import models
from users.models import NULLABLE


class Course(models.Model):

    title = models.CharField(max_length=250, verbose_name='название курса')
    preview = models.ImageField(upload_to='course/', verbose_name='превью (картинка)', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
