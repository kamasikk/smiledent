from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='ПІБ')),
                ('slug', models.SlugField(blank=True, max_length=170, unique=True, verbose_name='URL-адреса')),
                ('specialty', models.CharField(max_length=150, verbose_name='Спеціалізація')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='doctors/', verbose_name='Фото')),
                ('experience_years', models.PositiveSmallIntegerField(default=1, verbose_name='Стаж (років)')),
                ('education', models.TextField(blank=True, verbose_name='Освіта та сертифікати')),
                ('bio', models.TextField(verbose_name='Про лікаря')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок показу')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активний')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
            ],
            options={
                'verbose_name': 'Лікар',
                'verbose_name_plural': 'Лікарі',
                'ordering': ['order', 'full_name'],
            },
        ),
    ]
