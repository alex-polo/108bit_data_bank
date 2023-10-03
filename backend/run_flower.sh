#!/bin/bash
export CELERY_TYPE=FLOWER
venv/bin/celery -A server.tasks.main:app flower