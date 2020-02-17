from container import Container


class MessageWriter:
    def __init__(self, message_formatter=None):
        if message_formatter:
            self.message_formatter = message_formatter
        else:
            self.message_formatter = Container.message_formatter()

    def write(self, message):
        print(self.message_formatter.success(message))
