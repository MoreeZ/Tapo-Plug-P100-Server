# Tapo Smart Plug P100 Controller

A full-stack application to control TP-Link Tapo P100 Smart Plugs with a FastAPI backend and a responsive web interface.

## Project Structure

The project is divided into two main components:

- `client/`: Web interface to control the smart plug
- `server/`: FastAPI server that communicates with the Tapo P100 device

## Features

- Control Tapo P100 smart plugs via a web interface
- Turn the plug on and off via HTTP endpoints
- Trigger the plug to turn on for 5 seconds
- Easy to use RESTful API
- Responsive web interface

## Setup

### 1. Clone the repository:
```
git clone https://github.com/MoreeZ/Tapo-Plug-P100-Server.git
cd Tapo-Plug-P100-Server
```

### 2. Server Setup

1. Install server dependencies:
   ```
   cd server
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the server directory with your Tapo credentials (see `.env.example`):
   ```
   TAPO_USERNAME=your_email@example.com
   TAPO_PASSWORD=your_password
   TAPO_IP=192.168.x.x
   ```

### 3. Client Setup

The client is a static web application that can be served directly without additional installation steps.

## Usage

### Starting the Server

```
cd server
python main.py
```

The server will start on http://0.0.0.0:8000

### Opening the Client

Open `client/index.html` in your web browser to access the user interface.

## API Endpoints

- `GET /on` - Turn the plug on
- `GET /off` - Turn the plug off
- `GET /trigger` - Turn the plug on for 5 seconds, then off

## License

MIT
