#!/bin/bash
set -e

# Ensure .env file exists
if [ ! -f .env ]; then
    echo "ERROR: .env file not found in $(pwd)"
    echo "Please create a .env file with the required environment variables:"
    echo "TAPO_USERNAME, TAPO_PASSWORD, TAPO_IP, SERVER_LOCAL_ADDRESS, SERVER_LOCAL_PORT"
    exit 1
fi

echo "Loading environment variables from .env..."
export $(grep -v '^#' .env | xargs)

# Configuration from environment variables
IMAGE_NAME="${IMAGE_NAME:-server-tapo-server}"
CONTAINER_NAME="${CONTAINER_NAME:-tapo-server}"
HOST_PORT="${SERVER_LOCAL_PORT:-80}"
CONTAINER_PORT="${SERVER_LOCAL_PORT:-80}"

# Validate required variables for the Tapo server
if [ -z "$TAPO_USERNAME" ] || [ -z "$TAPO_PASSWORD" ] || [ -z "$TAPO_IP" ] || [ -z "$SERVER_LOCAL_ADDRESS" ] || [ -z "$SERVER_LOCAL_PORT" ]; then
    echo "ERROR: Missing required TAPO_* or SERVER_* environment variables in .env"
    exit 1
fi

echo "Stopping and removing any existing container..."
docker stop $CONTAINER_NAME >/dev/null 2>&1 || true
docker rm $CONTAINER_NAME >/dev/null 2>&1 || true

echo "Rebuilding Docker image: $IMAGE_NAME"
docker build -t $IMAGE_NAME .

echo "Starting new container: $CONTAINER_NAME on host port $HOST_PORT -> container port $CONTAINER_PORT"
docker run -d --name $CONTAINER_NAME --env-file .env -p $HOST_PORT:$CONTAINER_PORT $IMAGE_NAME

# Print access URL
HOST_IP=$(hostname -I | awk '{print $1}')
echo "Tapo Server is running at: http://$HOST_IP:$HOST_PORT/"
