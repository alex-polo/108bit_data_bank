import server


if __name__ == '__main__':
    try:
        server.run()
    except KeyboardInterrupt as interrupt:
        print(interrupt)
    except Exception as error:
        print(error)
