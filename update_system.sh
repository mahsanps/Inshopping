#!/bin/bash

# Update the system packages
echo "Updating system packages..."
sudo apt-get update && sudo apt-get upgrade -y

# Restart Docker service
echo "Restarting Docker service..."
sudo systemctl restart docker

# Rebuild the Docker containers
echo "Rebuilding Docker containers..."
docker-compose down
docker-compose up -d --build

# Check the status of Docker containers
echo "Checking Docker containers status..."
docker ps

# Check if the nginx container is running
echo "Checking if nginx container is running..."
docker ps | grep nginx

# Print a message indicating that the update is complete
echo "System update complete."
