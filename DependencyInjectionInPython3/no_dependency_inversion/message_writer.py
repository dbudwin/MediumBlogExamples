from message_formatter import MessageFormatter


class MessageWriter:
    def __init__(self):
        self.message_formatter = MessageFormatter()

    def write(self, message):
        print(self.message_formatter.success(message))
