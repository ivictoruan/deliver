release: python3 manage.py migrate
web: gunicorn deliver.wsgi --preload --log-file - 