import pytest
from websocket import create_connection

def test_websocket_connection():
    ws = create_connection("wss://echo.websocket.org")

    message = "Hello, WebSocket"
    ws.send(message)
    result = ws.recv()

    ws.close()
    assert result == message
