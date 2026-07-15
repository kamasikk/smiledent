import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name="Повне ім'я")),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Введіть коректний номер телефону, наприклад +380 XX XXX XX XX.', regex='^\\+?[0-9\\s\\-\\(\\)]{10,20}$')], verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('preferred_date', models.DateField(verbose_name='Бажана дата')),
                ('preferred_time', models.TimeField(verbose_name='Бажаний час')),
                ('message', models.TextField(blank=True, verbose_name='Коментар')),
                ('status', models.CharField(choices=[('new', 'Нова'), ('confirmed', 'Підтверджена'), ('cancelled', 'Скасована'), ('completed', 'Виконана')], default='new', max_length=20, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення заявки')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='doctors.doctor', verbose_name='Лікар')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='services.service', verbose_name='Послуга')),
            ],
            options={
                'verbose_name': 'Запис на прийом',
                'verbose_name_plural': 'Записи на прийом',
                'ordering': ['-created_at'],
            },
        ),
    ]
