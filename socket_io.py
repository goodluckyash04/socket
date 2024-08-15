import socketio
from socketio import ASGIApp
import urllib


ALLOWED_HOST = ['http://192.168.1.20:1234', 'http://localhost:1234']

# Create a Socket.IO server instance
sio = socketio.AsyncServer(cors_allowed_origins=ALLOWED_HOST,async_mode="asgi",logger=True)
sio_app = ASGIApp(sio)

active_client = {}

@sio.event
async def connect(sid, environ):
    client_code = urllib.parse.parse_qs(environ['QUERY_STRING']).get("client_code",None)
    if client_code:
        active_client.update({client_code[0]: sid})
        print("Active Client:", active_client)
    print("Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)

@sio.event
async def message(sid, data):
    print("message",data)
    await sio.emit('response', f"Message received: {sid}", to=sid)

# sonnected =  { 'QUERY_STRING': 'EIO=4&transport=websocket', 'RAW_URI': '/socket.io/?EIO=4&transport=websocket', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'REMOTE_ADDR': '127.0.0.1', 'REMOTE_PORT': '0', 'SERVER_NAME': 'asgi', 'SERVER_PORT': '0', 'asgi.receive': <bound method WebSocketProtocol.asgi_receive of <uvicorn.protocols.websockets.websockets_impl.WebSocketProtocol object at 0x0000025529AA1F10>>, 'asgi.send': <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x0000025529AB68E0>, 'asgi.scope': {'type': 'websocket', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'scheme': 'ws', 'server': ('::1', 8596), 'client': ('::1', 60611), 'root_path': '', 'path': '/socket.io/', 'raw_path': b'/socket.io/', 'query_string': b'EIO=4&transport=websocket', 'headers': [(b'host', b'localhost:8596'), (b'connection', b'Upgrade'), (b'pragma', b'no-cache'), (b'cache-control', b'no-cache'), (b'user-agent', b'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'), (b'upgrade', b'websocket'), (b'origin', b'http://localhost:1234'), (b'sec-websocket-version', b'13'), (b'accept-encoding', b'gzip, deflate, br, zstd'), (b'accept-language', b'en-IN,en;q=0.9'), (b'sec-websocket-key', b'/DJItwhDzw4pn3K9ProrBA=='), (b'sec-websocket-extensions', b'permessage-deflate; client_max_window_bits')], 'subprotocols': [], 'state': {}, 'extensions': {'websocket.http.response': {}}, 'app': <fastapi.applications.FastAPI object at 0x00000255296CD2B0>, 'starlette.exception_handlers': ({<class 'starlette.exceptions.HTTPException'>: <function http_exception_handler at 0x00000255294A4A40>, <class 'starlette.exceptions.WebSocketException'>: <bound method ExceptionMiddleware.websocket_exception of <starlette.middleware.exceptions.ExceptionMiddleware object at 0x00000255294D4CE0>>, <class 'fastapi.exceptions.RequestValidationError'>: <function request_validation_exception_handler at 0x00000255294A4B80>, <class 'fastapi.exceptions.WebSocketRequestValidationError'>: <function websocket_request_validation_exception_handler at 0x00000255294A4C20>}, {}), 'router': <fastapi.routing.APIRouter object at 0x00000255296CD220>, 'path_params': {}, 'app_root_path': '', 'endpoint': <socketio.asgi.ASGIApp object at 0x0000025529528920>}, 'HTTP_HOST': 'localhost:8596', 'HTTP_CONNECTION': 'Upgrade', 'HTTP_PRAGMA': 'no-cache', 'HTTP_CACHE_CONTROL': 'no-cache', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36', 'HTTP_UPGRADE': 'websocket', 'HTTP_ORIGIN': 'http://localhost:1234', 'HTTP_SEC_WEBSOCKET_VERSION': '13', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br, zstd', 'HTTP_ACCEPT_LANGUAGE': 'en-IN,en;q=0.9', 'HTTP_SEC_WEBSOCKET_KEY': '/DJItwhDzw4pn3K9ProrBA==', 'HTTP_SEC_WEBSOCKET_EXTENSIONS': 'permessage-deflate; client_max_window_bits', 'wsgi.url_scheme': 'http'}
