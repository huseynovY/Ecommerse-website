# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tmart.settings")
app = Celery("Tmart")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# (venv) $ python3 -m celery -A Tmart worker -l info
# celery -A Tmart worker --beat --scheduler django --loglevel=info

