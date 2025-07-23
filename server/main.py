import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from plugp100.common.credentials import AuthCredential
from plugp100.new.device_factory import connect, DeviceConnectConfiguration
from plugp100.new.components.on_off_component import OnOffComponent
import uvicorn

# Load environment variables from .env file
load_dotenv()

# Tapo credentials & device IP from environment variables
TAPO_USERNAME = os.getenv("TAPO_USERNAME")
TAPO_PASSWORD = os.getenv("TAPO_PASSWORD")
TAPO_IP = os.getenv("TAPO_IP")
SERVER_LOCAL_ADDRESS = os.getenv("SERVER_LOCAL_ADDRESS")
SERVER_LOCAL_PORT = int(os.getenv("SERVER_LOCAL_PORT", "42069"))

app = FastAPI()

# Get the absolute path to the client directory
BASE_DIR = Path(__file__).resolve().parent.parent
CLIENT_DIR = BASE_DIR / 'client'

# Mount the static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory=CLIENT_DIR), name="static")


async def get_plug() -> OnOffComponent:
    """
    Connect to the plug and return the OnOffComponent.
    """
    credentials = AuthCredential(TAPO_USERNAME, TAPO_PASSWORD)
    config = DeviceConnectConfiguration(
        host=TAPO_IP,
        credentials=credentials
    )

    device = await connect(config)
    await device.update()

    # Find the OnOffComponent
    plug = device.get_component(OnOffComponent)
    if not plug:
        raise RuntimeError("OnOffComponent not found on this device.")
    return plug


@app.get("/on")
async def turn_on():
    """
    Turn the plug on.
    """
    try:
        plug = await get_plug()
        await plug.turn_on()
        return {"status": "on"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/off")
async def turn_off():
    """
    Turn the plug off.
    """
    try:
        plug = await get_plug()
        await plug.turn_off()
        return {"status": "off"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def read_root():
    """
    Serve the client application's index.html file.
    """
    return FileResponse(CLIENT_DIR / "index.html")


@app.get("/trigger")
async def trigger_five_seconds():
    """
    Turn the plug on and then automatically turn it off after 3 seconds.
    """
    try:
        plug = await get_plug()
        
        # Turn on
        await plug.turn_on()
        
        # Wait for 3 seconds
        await asyncio.sleep(3)
        
        # Turn off
        await plug.turn_off()
        
        return {"status": "triggered", "message": "Plug was turned on for 3 seconds"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("server:app", host=SERVER_LOCAL_ADDRESS, port=SERVER_LOCAL_PORT, reload=True)
