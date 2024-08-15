import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from socket_io import sio_app
import api_router

app = FastAPI()
endpoint = FastAPI()


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


if __name__ == "__main__":
    uvicorn.run('main:app', host="localhost", port=8596)