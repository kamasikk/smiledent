# SmileDent — Преміальний сайт стоматологічної клініки

Django-проєкт сучасної стоматологічної клініки з онлайн-записом, каталогом
лікарів, послуг, цін, відгуків та FAQ.

## Технології
- Python 3.12 / Django 5.1
- SQLite (dev) → PostgreSQL (production, через `DATABASE_URL`)
- HTML5 / CSS3 (без фреймворків, кастомний дизайн) / Vanilla JS
- Gunicorn + WhiteNoise для деплою на Render

## Швидкий старт (локально)

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env             # і за потреби відредагуйте значення

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Сайт буде доступний на http://127.0.0.1:8000/, адмінка — на
http://127.0.0.1:8000/admin/.

## Деплой на Render

1. Запуште репозиторій на GitHub.
2. У Render оберіть "New Blueprint" і вкажіть цей репозиторій —
   `render.yaml` автоматично налаштує web-сервіс та PostgreSQL базу.
3. Після першого деплою виконайте `createsuperuser` через Render Shell.

## Структура застосунків

| Застосунок     | Призначення                                  |
|----------------|-----------------------------------------------|
| `core`         | Головна, про клініку, FAQ, контакти           |
| `doctors`      | Каталог лікарів (CRUD через адмінку)          |
| `services`     | Послуги та прайс-лист (CRUD через адмінку)    |
| `reviews`      | Відгуки пацієнтів (CRUD + модерація)          |
| `appointments` | Форма онлайн-запису з валідацією              |

## SEO

- Унікальні `<title>` та meta description на кожній сторінці.
- Семантична розмітка, один `<h1>` на сторінку.
- `robots.txt`, `sitemap.xml`, Open Graph теги.
- `alt`-атрибути для всіх зображень.
