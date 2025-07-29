#!/bin/bash

# Name for the Docker image and container
IMAGE_NAME="server-tapo-server"
CONTAINER_NAME="tapo-server"

echo "Stopping and removing any existing container..."
docker stop $CONTAINER_NAME >/dev/null 2>&1 || true
docker rm $CONTAINER_NAME >/dev/null 2>&1 || true

echo "Rebuilding Docker image..."
docker build -t $IMAGE_NAME .

echo "Starting new container on port 80..."
docker run -d --name $CONTAINER_NAME -p 80:80 $IMAGE_NAME

echo "Tapo Server is running at: http://$(hostname -I | awk '{print $1}')/"
