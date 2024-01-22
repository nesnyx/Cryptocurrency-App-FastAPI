from fastapi import APIRouter, Request,Form
from fastapi.responses import HTMLResponse
from typing import Optional
from fastapi.templating import Jinja2Templates
from api import get_listing
router = APIRouter()

templates = Jinja2Templates(directory="templates")
@router.get('/')
async def home(request : Request):
    return templates.TemplateResponse('home.html', {
        'request' : request,
        
    })

@router.get('/listing')
async def listing(request: Request):
    data = get_listing()
    return templates.TemplateResponse('search.html',{
        'request' : request,
        'data' : data
    })

@router.get('/listing/{id}')
async def get_byId(request: Request, id:int):
    data = get_listing()
    for i in data:
        if i['id'] == id:
            storage = {
                'name' : i['name'],
                'id' : i['id'],
                'symbol' : i['symbol'],
                "total_supply" : i['total_supply'],
                'last_updated' : i['last_updated']
            }
            
    return templates.TemplateResponse('detail.html',{
        'request' : request,
        'data' : storage
    })

@router.get('/about')
async def about(request:Request):
    return templates.TemplateResponse('about.html',{
        'request' : request
    })
