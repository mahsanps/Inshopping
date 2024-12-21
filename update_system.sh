#!/bin/sh
set -e

cd /root/inshopping/Inshopping || exit 1

git fetch
git pull

docker-compose down

docker-compose build

docker-compose up -d
