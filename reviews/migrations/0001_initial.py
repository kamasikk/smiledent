from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, verbose_name="Ім'я пацієнта")),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5, verbose_name='Оцінка')),
                ('text', models.TextField(verbose_name='Текст відгуку')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='reviews/', verbose_name='Фото пацієнта')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Схвалено до публікації')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
                'ordering': ['-created_at'],
            },
        ),
    ]
