from fastapi import FastAPI, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.database import engine, get_db
from db import models, schemas

from routes import chat, chatlist, stt

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/api")

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello" : "World"}

app.include_router(router)
app.include_router(chatlist.router)
app.include_router(stt.router)
app.include_router(chat.router)