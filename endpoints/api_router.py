from fastapi import APIRouter

from socket_events.socket_io import active_client, sio, get_client_code

router = APIRouter()

@router.get('/active-clients')
def get_active_clients():
    return {"client_list":list(active_client.keys())}

@router.get('/active-participants')
def get_active_clients():
    content = []
    namespace = "/"
    room = None
    for i,j in sio.manager.get_participants(namespace,room):
        content.append({
            "client":get_client_code(i),
            "sid":i,
            "extra":j
        })
    return {"data":content}



