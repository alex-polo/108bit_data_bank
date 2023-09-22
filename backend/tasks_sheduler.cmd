set CELERY_TYPE=BEAT
venv\Scripts\celery.exe -A server.tasks.main:app beat