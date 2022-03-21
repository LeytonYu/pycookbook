import time

import websocket
import json

ws = websocket.WebSocket()
ws.connect("ws://localhost:10001/chat/unit/")
msg = 'Роза 234567890'
link = {
    'command': 'link',
    'pwd': 'yld971202',
    'unit': 25,
    'mtype': 2,
    'user': 102475,
    'admin': 110669
}
ws.send(json.dumps(link))
content = {
    'command': 'return',
    'message': msg,
    'pwd': 'yld971202',
    'unit': 25,
    'user': 102475,
    'mtype': 2,
    'admin': 110669
}

count = 1
# while True:
#     time.sleep(20)
ws.send(json.dumps(content))
count += 1
msg = f"{msg}_{count}"
content['message'] = msg
print(ws.recv())
ws.close()