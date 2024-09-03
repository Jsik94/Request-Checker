from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse , Response
from urllib.parse import urlparse,parse_qs
import os
import json

# router = APIRouter(prefix='/test',tags=['test'])
router = APIRouter()


# llm 단건
@router.post("/")
async def test1(request : Request):
    
    print(request)

    return "default response"

