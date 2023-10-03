export CELERY_TYPE=FLOWER
venv/bin/celery -A server.tasks.main:app worker --hostname=data_bank@$hostname
