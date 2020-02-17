import pytest

from message_writer import MessageWriter


@pytest.fixture
def mock_message_formatter(mocker):
    return mocker.patch("message_formatter.MessageFormatter")


def test_write_calls_message_formatter_success_once_with_value(mock_message_formatter):
    message_writer = MessageWriter(mock_message_formatter)
    message = "Hello World!"

    message_writer.write(message)

    mock_message_formatter.success.assert_called_once_with(message)
