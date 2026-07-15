from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва категорії')),
                ('slug', models.SlugField(blank=True, max_length=120, unique=True, verbose_name='URL-адреса')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок показу')),
            ],
            options={
                'verbose_name': 'Категорія послуг',
                'verbose_name_plural': 'Категорії послуг',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва послуги')),
                ('slug', models.SlugField(blank=True, max_length=170, unique=True, verbose_name='URL-адреса')),
                ('short_description', models.CharField(max_length=255, verbose_name='Короткий опис')),
                ('description', models.TextField(verbose_name='Повний опис')),
                ('icon', models.CharField(choices=[('tooth', 'Зуб'), ('implant', 'Імплант'), ('braces', 'Брекети'), ('whitening', 'Відбілювання'), ('checkup', 'Огляд'), ('surgery', 'Хірургія'), ('kids', 'Дитяча стоматологія'), ('cleaning', 'Гігієна')], default='tooth', max_length=50, verbose_name='Іконка')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='Зображення')),
                ('price_from', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна від (грн)')),
                ('duration_minutes', models.PositiveIntegerField(default=30, verbose_name='Тривалість (хв)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок показу')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='services.servicecategory', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Послуга',
                'verbose_name_plural': 'Послуги',
                'ordering': ['order', 'name'],
            },
        ),
    ]
