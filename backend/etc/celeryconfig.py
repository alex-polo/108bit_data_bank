from kombu import Queue

worker_hijack_root_logger = False

broker_connection_retry_on_startup = True
task_remote_tracebacks = True
database_engine_options = {'echo': True}
timezone = 'Europe/Moscow'

task_queues = (
    Queue('default', exchange='default', routing_key='task_default', max_priority=100),
    Queue('data_collection', exchange='data_collection', routing_key='task_data_collection', max_priority=100),
)

task_default_queue = 'default'

task_routes = {'server.tasks.v1.*': {'queue': 'data_collection'}}

# task_routes = {
#         'server.tasks.v1.*': {
#             'queue': 'data_collection',
#             'routing_key': 'task_data_collection',
#         },
# }

worker_deduplicate_successful_tasks = True
worker_concurrency = 4
