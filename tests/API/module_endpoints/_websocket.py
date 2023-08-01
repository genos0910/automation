from websocket import create_connection

def test_websocket_api():
    ws = create_connection("wss://echo.websocket.org")
    ws.send("Hello, Websocket")
    result = ws.recv()
    assert result == "Hello, Websocket"
    ws.close()
