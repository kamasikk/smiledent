from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    """Відгук пацієнта клініки."""
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    author_name = models.CharField("Ім'я пацієнта", max_length=100)
    rating = models.PositiveSmallIntegerField(
        'Оцінка', choices=RATING_CHOICES, default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    text = models.TextField('Текст відгуку')
    photo = models.ImageField('Фото пацієнта', upload_to='reviews/', blank=True, null=True)
    is_approved = models.BooleanField('Схвалено до публікації', default=False)
    created_at = models.DateTimeField('Дата створення', auto_now_add=True)

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author_name} ({self.rating}/5)'

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return f'https://i.pravatar.cc/150?u=review{self.pk}'

    @property
    def stars_range(self):
        return range(self.rating)

    @property
    def empty_stars_range(self):
        return range(5 - self.rating)
