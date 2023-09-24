import server
import logging.config
import traceback

from logging import Logger


def logging_configure() -> Logger:
    logging.config.fileConfig('etc/server_logging.ini')
    return logging.getLogger(__name__)


if __name__ == '__main__':
    logger = logging_configure()

    try:
        logger.info('Starting API Server')
        server.run()
    except KeyboardInterrupt as interrupt:
        logger.error('API server stopped')
    except Exception as error:
        logger.error(error)
        logger.error(traceback.format_exc(limit=None, chain=True))

