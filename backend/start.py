import server
from server.config import get_api_server_config

if __name__ == '__main__':
    try:
        config_server = get_api_server_config()
        server.run(config_server=config_server)
        print(config_server)

    except KeyboardInterrupt as interrupt:
        print('API server stopped')
    except Exception as error:
        print(error)
