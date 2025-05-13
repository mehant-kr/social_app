release: python manage.py tailwind install && python manage.py tailwind build && python manage.py collectstatic --noinput
web: gunicorn social_app.wsgi