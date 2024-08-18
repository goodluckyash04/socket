from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from socket_events.socket_io import sio_app
from endpoints import api_router

app = FastAPI()


# Allow React frontend to communicate with the server
ORIGINS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(api_router.router)


# Attach the Socket.IO,endpoint server to the FastAPI app
app.mount("/",sio_app)

