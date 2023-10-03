#!/bin/bash
export CELERY_TYPE=BEAT
venv/bin/celery -A server.tasks.main:app beat