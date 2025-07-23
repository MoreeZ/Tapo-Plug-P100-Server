import asyncio
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
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

app = FastAPI()


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


@app.get("/trigger")
async def trigger_five_seconds():
    """
    Turn the plug on and then automatically turn it off after 5 seconds.
    """
    try:
        plug = await get_plug()
        
        # Turn on
        await plug.turn_on()
        
        # Wait for 5 seconds
        await asyncio.sleep(5)
        
        # Turn off
        await plug.turn_off()
        
        return {"status": "triggered", "message": "Plug was turned on for 5 seconds"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
