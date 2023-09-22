set CELERY_TYPE=WORKER
venv\Scripts\celery.exe -A server.tasks.main:app worker --pool=solo --hostname=data_bank@%hostname%