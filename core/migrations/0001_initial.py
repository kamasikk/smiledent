from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Питання')),
                ('answer', models.TextField(verbose_name='Відповідь')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок показу')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубліковано')),
            ],
            options={
                'verbose_name': 'Питання (FAQ)',
                'verbose_name_plural': 'FAQ — Часті запитання',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('subject', models.CharField(blank=True, max_length=150, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Повідомлення')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата надсилання')),
            ],
            options={
                'verbose_name': 'Повідомлення з форми контактів',
                'verbose_name_plural': 'Повідомлення з контактів',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=255, verbose_name='Опис')),
                ('icon', models.CharField(choices=[('shield', 'Щит (безпека)'), ('star', 'Зірка (якість)'), ('clock', 'Годинник (час)'), ('heart', 'Серце (турбота)'), ('tooth', 'Зуб (стоматологія)'), ('award', 'Нагорода (досвід)')], default='shield', max_length=50, verbose_name='Іконка')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок показу')),
            ],
            options={
                'verbose_name': 'Перевага клініки',
                'verbose_name_plural': 'Переваги клініки',
                'ordering': ['order', 'id'],
            },
        ),
    ]
