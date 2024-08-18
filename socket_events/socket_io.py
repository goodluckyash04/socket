import socketio
from socketio import ASGIApp
import urllib


ALLOWED_HOST = ['http://192.168.1.20:1234', 'http://localhost:1234']

# Create a Socket.IO server instance
sio = socketio.AsyncServer(cors_allowed_origins=ALLOWED_HOST,async_mode="asgi",logger=True)
sio_app = ASGIApp(sio)

active_client = {}
def get_client_code(sid):
    for i, j in active_client.copy().items():
        if j == sid:
            return i
    return None

@sio.event
async def connect(sid, environ):
    client_code = urllib.parse.parse_qs(environ['QUERY_STRING']).get("client",None)
    if not client_code:
        await sio.disconnect(sid)
        print(f"disconnected:", sid)
        return 0

    if client_code[0] in active_client:
        await sio.disconnect(active_client[client_code[0]])

    active_client.update({client_code[0]:sid})
    print(f"{client_code[0]} connected:", sid )
    # for i in sio.manager.get_participants('/',None):
    #     print(i)
@sio.event
async def disconnect(sid):
    client = get_client_code(sid)
    if client:
        del active_client[client]
    print("Client disconnected:",sid, client)

@sio.event
async def message(sid, data):
    print("message",data)
    client = get_client_code(sid)

    content = {
        "client":client if client else sid,
        "data":data
    }
    await sio.emit('response', content)

