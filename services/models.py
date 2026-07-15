from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ServiceCategory(models.Model):
    """Категорія послуг (Терапія, Хірургія, Ортодонтія тощо)."""
    name = models.CharField('Назва категорії', max_length=100)
    slug = models.SlugField('URL-адреса', max_length=120, unique=True, blank=True)
    order = models.PositiveIntegerField('Порядок показу', default=0)

    class Meta:
        verbose_name = 'Категорія послуг'
        verbose_name_plural = 'Категорії послуг'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=False) or 'category'
        super().save(*args, **kwargs)


class Service(models.Model):
    """Стоматологічна послуга з описом та ціною."""
    ICON_CHOICES = [
        ('tooth', 'Зуб'),
        ('implant', 'Імплант'),
        ('braces', 'Брекети'),
        ('whitening', 'Відбілювання'),
        ('checkup', 'Огляд'),
        ('surgery', 'Хірургія'),
        ('kids', 'Дитяча стоматологія'),
        ('cleaning', 'Гігієна'),
    ]

    category = models.ForeignKey(
        ServiceCategory, verbose_name='Категорія', related_name='services',
        on_delete=models.SET_NULL, null=True, blank=True,
    )
    name = models.CharField('Назва послуги', max_length=150)
    slug = models.SlugField('URL-адреса', max_length=170, unique=True, blank=True)
    short_description = models.CharField('Короткий опис', max_length=255)
    description = models.TextField('Повний опис')
    icon = models.CharField('Іконка', max_length=50, choices=ICON_CHOICES, default='tooth')
    image = models.ImageField('Зображення', upload_to='services/', blank=True, null=True)
    price_from = models.DecimalField('Ціна від (грн)', max_digits=10, decimal_places=2)
    duration_minutes = models.PositiveIntegerField('Тривалість (хв)', default=30)
    order = models.PositiveIntegerField('Порядок показу', default=0)
    is_active = models.BooleanField('Активна', default=True)
    created_at = models.DateTimeField('Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField('Дата оновлення', auto_now=True)

    class Meta:
        verbose_name = 'Послуга'
        verbose_name_plural = 'Послуги'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name, allow_unicode=False) or 'service'
            slug = base_slug
            counter = 1
            while Service.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f'{base_slug}-{counter}'
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return f'https://picsum.photos/seed/{self.slug or self.pk}/800/600'
