from django.conf import settings
from django.db import models


from course.models import Course
from lesson.models import Lesson
from users.models import NULLABLE


class Payment(models.Model):

    CASH = 'cash'
    TRANSFER_TO_ACCOUNT = 'transfer to account'

    PAYMENT_METHOD = (
        (CASH, 'Наличными'),
        (TRANSFER_TO_ACCOUNT, 'Перевод на счет')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь',
                             **NULLABLE)
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченый курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченый урок', **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, verbose_name='Способ оплаты')

    def __str__(self):
        return f"{self.user} - {self.payment_amount}"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
