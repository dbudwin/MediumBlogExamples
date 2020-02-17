from dependency_injector import containers, providers

from message_formatter import MessageFormatter


class Container(containers.DeclarativeContainer):
    message_formatter = providers.Factory(MessageFormatter)
