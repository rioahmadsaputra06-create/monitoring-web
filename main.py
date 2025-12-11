from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

devices = [
    {"name": "Router A", "status": "online", "bandwidth": 20},
    {"name": "Router B", "status": "offline", "bandwidth": 0},
    {"name": "Router C", "status": "online", "bandwidth": 35},
]

@app.get("/")
def root():
    return {"message": "Web Monitoring berjalan!"}

@app.get("/devices")
def get_devices():
    for d in devices:
        d["bandwidth"] = random.randint(5, 50)
    return devices
