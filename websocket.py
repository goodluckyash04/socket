# import uvicorn
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.middleware.cors import CORSMiddleware
#
# app = FastAPI()
#
# # Allow React frontend to communicate with the server
# origins = [
#     "http://localhost:3000",  # React development server
#     # Add more origins if needed
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await websocket.send_text(f"Message received: {data}")
#     except WebSocketDisconnect:
#         print("Client disconnected")
#
# if __name__ == '__main__':
#     uvicorn.run(app,host="localhost",port=8000)