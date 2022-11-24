import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('app')


app.config_from_object('django_conf:settings', namespace='CELERY')


app.autodiscover_tasks()

@app.task(bind=True)
def csv_export(self):
    print("This is an export task!")
