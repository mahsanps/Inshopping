#!/bin/bash

# Exit immediately if a command exits with a non-zero status (optional)
set -e

# ---------------------------------------------------------
# Function to "try" a command, and "catch" if it fails
# ---------------------------------------------------------
try_command() {
  # $1 = command to run (string)
  # $2 = error message if command fails (string)

  # Evaluate the command
  if eval "$1"; then
    echo "Command succeeded: $1"
  else
    echo "ERROR: $2" 1>&2
    # Decide if you want to exit or continue
    # exit 1
  fi
}

git fetch
git pull

# ---------------------------------------------------------
# 1) Stop & disable any system-level Nginx
# ---------------------------------------------------------
echo "Attempting to stop and disable host-level Nginx if running..."

try_command \
  "sudo systemctl stop nginx" \
  "Failed to stop nginx. Check if nginx is installed/running."

try_command \
  "sudo systemctl disable nginx" \
  "Failed to disable nginx. Check if nginx is installed/running."

# ---------------------------------------------------------
# Update the system packages
# ---------------------------------------------------------
echo "Updating system packages..."
sudo apt-get update && sudo apt-get upgrade -y

# ---------------------------------------------------------
# Check if the nginx container is running
# ---------------------------------------------------------
echo "Checking if nginx container is running..."
docker ps | grep nginx || echo "nginx container not found."

# ---------------------------------------------------------
# Rebuild Docker containers
# ---------------------------------------------------------
echo "Rebuilding Docker containers..."
docker-compose down
docker-compose up -d --build



# ---------------------------------------------------------
# Check Docker containers status
# ---------------------------------------------------------
echo "Checking Docker containers status..."
docker ps



# ---------------------------------------------------------
# Print a completion message
# ---------------------------------------------------------
echo "System update complete."
