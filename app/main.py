from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import dotenv
import os
from starlette.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocket
from api.main import api_router
import asyncio
import logging

dotenv.load_dotenv()


app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static") 

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn.error")


app.include_router(api_router)


connected_websockets = []

# Middleware to log all requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    # 요청 정보를 모든 연결된 웹소켓에 전송
    message = f"Request: {request.method} {request.url}\n"
    print('middleware msg :',message)
    await broadcast_message(message)
    return response

# 웹소켓으로 메시지 전송
async def broadcast_message(message: str):
    for websocket in connected_websockets:
        await websocket.send_text(message)


# 웹소켓 라우트
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_websockets.append(websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        logger.error(f"WebSocket connection error: {e}")
    finally:
        connected_websockets.remove(websocket)
        await websocket.close()


@app.get('/')
async def main() -> dict : 

    return RedirectResponse(url="/docs")


if __name__ =="__main__":
    # app.run(debug=True, host="0.0.0.0",port=int(os.environ.get("PORT",8100)))
    # import sys
    # print(sys.path)
    pass