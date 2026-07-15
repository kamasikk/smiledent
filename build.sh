#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Завантажуємо демо-дані (лікарі, послуги, відгуки, FAQ).
# loaddata безпечно виконувати повторно — записи з тими самими pk оновляться, а не задваяться.
python manage.py loaddata core/fixtures/initial_data.json

# Автоматично створюємо суперкористувача (без інтерактивного Shell),
# якщо в Environment на Render задані відповідні змінні.
python manage.py shell << 'PYEOF'
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f'Суперкористувача "{username}" створено.')
    else:
        print(f'Суперкористувач "{username}" уже існує — пропускаємо.')
else:
    print('DJANGO_SUPERUSER_USERNAME/PASSWORD не задані — суперкористувача не створено.')
PYEOF
