from django.db import models


class FAQ(models.Model):
    """Часті запитання, що виводяться на сторінці FAQ та частково на головній."""
    question = models.CharField('Питання', max_length=255)
    answer = models.TextField('Відповідь')
    order = models.PositiveIntegerField('Порядок показу', default=0)
    is_published = models.BooleanField('Опубліковано', default=True)

    class Meta:
        verbose_name = 'Питання (FAQ)'
        verbose_name_plural = 'FAQ — Часті запитання'
        ordering = ['order', 'id']

    def __str__(self):
        return self.question


class ContactMessage(models.Model):
    """Повідомлення, надіслані через форму зворотного зв'язку."""
    name = models.CharField("Ім'я", max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20, blank=True)
    subject = models.CharField('Тема', max_length=150, blank=True)
    message = models.TextField('Повідомлення')
    is_read = models.BooleanField('Прочитано', default=False)
    created_at = models.DateTimeField('Дата надсилання', auto_now_add=True)

    class Meta:
        verbose_name = 'Повідомлення з форми контактів'
        verbose_name_plural = 'Повідомлення з контактів'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.subject or "Без теми"}'


class Advantage(models.Model):
    """Переваги клініки для блоку 'Чому обирають нас' на головній сторінці."""
    ICON_CHOICES = [
        ('shield', 'Щит (безпека)'),
        ('star', 'Зірка (якість)'),
        ('clock', 'Годинник (час)'),
        ('heart', 'Серце (турбота)'),
        ('tooth', 'Зуб (стоматологія)'),
        ('award', 'Нагорода (досвід)'),
    ]

    title = models.CharField('Заголовок', max_length=100)
    description = models.CharField('Опис', max_length=255)
    icon = models.CharField('Іконка', max_length=50, choices=ICON_CHOICES, default='shield')
    order = models.PositiveIntegerField('Порядок показу', default=0)

    class Meta:
        verbose_name = 'Перевага клініки'
        verbose_name_plural = 'Переваги клініки'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title
