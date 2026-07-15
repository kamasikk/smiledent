from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Doctor(models.Model):
    """Профіль лікаря клініки."""
    full_name = models.CharField("ПІБ", max_length=150)
    slug = models.SlugField('URL-адреса', max_length=170, unique=True, blank=True)
    specialty = models.CharField('Спеціалізація', max_length=150)
    photo = models.ImageField('Фото', upload_to='doctors/', blank=True, null=True)
    experience_years = models.PositiveSmallIntegerField('Стаж (років)', default=1)
    education = models.TextField('Освіта та сертифікати', blank=True)
    bio = models.TextField('Про лікаря')
    order = models.PositiveIntegerField('Порядок показу', default=0)
    is_active = models.BooleanField('Активний', default=True)
    created_at = models.DateTimeField('Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField('Дата оновлення', auto_now=True)

    class Meta:
        verbose_name = 'Лікар'
        verbose_name_plural = 'Лікарі'
        ordering = ['order', 'full_name']

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.full_name, allow_unicode=False) or 'doctor'
            slug = base_slug
            counter = 1
            while Doctor.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f'{base_slug}-{counter}'
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('doctors:detail', kwargs={'slug': self.slug})

    @property
    def photo_url(self):
        """Повертає URL фото або якісне безкоштовне зображення-заглушку."""
        if self.photo:
            return self.photo.url
        return f'https://i.pravatar.cc/500?u={self.slug or self.pk}'
