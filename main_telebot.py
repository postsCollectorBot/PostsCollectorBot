from multiprocessing import Process
from building_main import run_telebot
from building_main import run_pyrogram
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    run_pyrogram()
    return {"message": "Hello World"}

