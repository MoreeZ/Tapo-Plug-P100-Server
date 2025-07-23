# Tapo Smart Plug P100 Server

A simple FastAPI server to control TP-Link Tapo P100 Smart Plugs.

## Features

- Turn the plug on and off via HTTP endpoints
- Trigger the plug to turn on for 5 seconds
- Easy to use RESTful API

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/MoreeZ/Tapo-Plug-P100-Server.git
   cd Tapo-Plug-P100-Server
   ```

2. Install dependencies:
   ```
   pip install fastapi uvicorn python-dotenv plugp100
   ```

3. Create a `.env` file with your Tapo credentials (see `.env.example`):
   ```
   TAPO_USERNAME=your_email@example.com
   TAPO_PASSWORD=your_password
   TAPO_IP=192.168.x.x
   ```

## Usage

Run the server:

```
python main.py
```

The server will start on http://0.0.0.0:8000

## API Endpoints

- `GET /on` - Turn the plug on
- `GET /off` - Turn the plug off
- `GET /trigger` - Turn the plug on for 5 seconds, then off

## License

MIT
