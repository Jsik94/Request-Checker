from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import RedirectResponse , Response
from urllib.parse import urlparse,parse_qs
import os
import json

# router = APIRouter(prefix='/test',tags=['test'])
router = APIRouter()
templates = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static") 

# llm 단건
@router.get("/", response_class=HTMLResponse)
async def get_console_page(request: Request):

    # 헤더 출력
    headers = dict(request.headers)
    print("Headers: ", json.dumps(headers, indent=4, ensure_ascii=False))

    # 바디 출력
    body = await request.body()
    try:
        # JSON 형식으로 바디 파싱 및 출력
        body_json = json.loads(body.decode('utf-8'))
        print("Body: ", json.dumps(body_json, indent=4, ensure_ascii=False))
    except json.JSONDecodeError:
        # JSON이 아닌 경우 그냥 출력
        print("Body: ", body.decode('utf-8'))
    return templates.TemplateResponse("console.html", {"request": request})