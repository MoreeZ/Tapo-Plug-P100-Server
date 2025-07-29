# Tapo Plug P100 Server

A simple FastAPI server to control your **TP-Link Tapo P100** smart plug.  
The server provides REST endpoints to turn the plug **on/off** and a small static client UI.

---

## ⚠️ Important Notice

This server **relies on the [plugp100](https://github.com/petretiandrea/plugp100) library** by **petretiandrea**,  
which is a fork of **[tapo-p100-python](https://k4czp3r.xyz/blog/post/reverse-engineering-tp-link-tapo)**  
by **K4CZP3R**.

- This project is **reverse-engineered** and **not officially supported by TP-Link**.  
- Functionality may **break in the future** if TP-Link updates the firmware or API.

---

A simple FastAPI server to control your **TP-Link Tapo P100** smart plug.  
The server provides REST endpoints to turn the plug **on/off** and a small static client UI.

---

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Tapo-Plug-P100-Server.git
cd Tapo-Plug-P100-Server
```

---

## 2. Setup Environment Variables

Create a `.env` file in the project root:

```ini
TAPO_USERNAME=your_email@example.com
TAPO_PASSWORD=your_password
TAPO_IP=192.168.x.x
SERVER_LOCAL_ADDRESS=192.168.x.x
SERVER_LOCAL_PORT=80
```

**Notes:**
- `TAPO_IP` = IP address of your Tapo plug on the local network  
- `SERVER_LOCAL_ADDRESS` = IP of your host machine (for accessing the server)  
- `SERVER_LOCAL_PORT` = Port exposed by the server (default: 80)  

---

## 3. Requirements

- Docker installed and running  
- No need to install Python dependencies locally — everything runs inside Docker

---

## 4. Deploy the Server

Run the deployment script:

```bash
./deploy_tapo_server.sh
```

This will:

1. Check that `.env` exists  
2. Build the Docker image  
3. Start a container on the port specified in `.env`  

If successful, you’ll see:

```
Tapo Server is running at: http://<SERVER_LOCAL_ADDRESS>:<SERVER_LOCAL_PORT>/
```

---

## 5. Verify the Server

Open your browser:

```
http://<SERVER_LOCAL_ADDRESS>:<SERVER_LOCAL_PORT>/
```

Or test the endpoints:

```bash
curl http://<SERVER_LOCAL_ADDRESS>:<SERVER_LOCAL_PORT>/on
curl http://<SERVER_LOCAL_ADDRESS>:<SERVER_LOCAL_PORT>/off
curl http://<SERVER_LOCAL_ADDRESS>:<SERVER_LOCAL_PORT>/trigger
```

---

## 6. Managing the Server

- **Check running containers**:

```bash
docker ps
```

- **View logs**:

```bash
docker logs <container_id>
```

- **Stop the server**:

```bash
docker stop <container_id>
```

---

You’re now ready to control your **Tapo Plug P100** from any browser or REST client on your local network.
