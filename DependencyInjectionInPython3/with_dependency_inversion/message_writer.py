class MessageWriter:
    def __init__(self, message_formatter):
        self.message_formatter = message_formatter

    def write(self, message):
        print(self.message_formatter.success(message))
