from message_formatter import MessageFormatter
from message_writer import MessageWriter


def main():
    message_formatter = MessageFormatter()
    message_writer = MessageWriter(message_formatter)
    message_writer.write("Hello World!")


if __name__ == "__main__":
    main()
