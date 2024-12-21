#!/bin/sh

# Optional: set script to exit on error
set -e

# 1. Navigate to your project directory
cd /app || exit 1

# 2. Fetch and pull the latest changes from your GitHub repository
git fetch
git pull

# 3. Build updated Docker images
docker-compose build

# 4. Spin up the containers (in the background)
docker-compose up -d
