from building_main import run_telebot
from fastapi import FastAPI

from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    await run_telebot()
    return {"message": "Hello World"}
