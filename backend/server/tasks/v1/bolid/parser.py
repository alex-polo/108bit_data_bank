from celery import shared_task


@shared_task()
def bolid_task() -> None:
    pass
