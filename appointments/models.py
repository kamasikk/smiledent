from django.core.validators import RegexValidator
from django.db import models

phone_validator = RegexValidator(
    regex=r'^\+?[0-9\s\-\(\)]{10,20}$',
    message='Введіть коректний номер телефону, наприклад +380 XX XXX XX XX.',
)


class Appointment(models.Model):
    """Заявка на онлайн-запис до стоматолога."""

    STATUS_NEW = 'new'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_CANCELLED = 'cancelled'
    STATUS_COMPLETED = 'completed'
    STATUS_CHOICES = [
        (STATUS_NEW, 'Нова'),
        (STATUS_CONFIRMED, 'Підтверджена'),
        (STATUS_CANCELLED, 'Скасована'),
        (STATUS_COMPLETED, 'Виконана'),
    ]

    full_name = models.CharField("Повне ім'я", max_length=150)
    phone = models.CharField('Телефон', max_length=20, validators=[phone_validator])
    email = models.EmailField('Email', blank=True)
    doctor = models.ForeignKey(
        'doctors.Doctor', verbose_name='Лікар', related_name='appointments',
        on_delete=models.SET_NULL, null=True, blank=True,
    )
    service = models.ForeignKey(
        'services.Service', verbose_name='Послуга', related_name='appointments',
        on_delete=models.SET_NULL, null=True, blank=True,
    )
    preferred_date = models.DateField('Бажана дата')
    preferred_time = models.TimeField('Бажаний час')
    message = models.TextField('Коментар', blank=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    created_at = models.DateTimeField('Дата створення заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Запис на прийом'
        verbose_name_plural = 'Записи на прийом'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} — {self.preferred_date} {self.preferred_time}'
