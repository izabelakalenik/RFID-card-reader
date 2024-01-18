from connect_to_server import Connection
from card_reader import RFIDReader


def main():
    connection = Connection()
    card_reader = RFIDReader()

    while True:
        result = card_reader.read()
        if result is not None:
            connection.send_authorization_request(str(result))


if __name__ == '__main__':
    main()
