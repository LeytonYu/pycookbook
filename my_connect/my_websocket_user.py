import websocket
import json

ws = websocket.WebSocket()
my_cookie = 'ctsessionid=t6bg29wr0f5scoho6dudj5piswvogid8; ' \
            'expires=Thu, 27 Jan 2022 02:12:02 GMT; HttpOnly; Max-Age=1209600; Path=/; SameSite=Lax'
ws.connect("ws://localhost:10001/chat/unit/", cookie=my_cookie)

content = {
    'command': 'join',
    'unit': 25,
}
content_t = {
    'command': 'send',
    'message': '我想吃桃子',
    'mtype': 2,
    'unit': 25
}
ws.send(json.dumps(content))
ws.send(json.dumps(content_t))
print(ws.recv())
ws.close()
