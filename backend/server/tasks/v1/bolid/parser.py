from celery import shared_task


@shared_task()
def task() -> None:
    print(11111111111111111111)
    pass
