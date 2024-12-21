#!/bin/bash
set -e

# Wait for PostgreSQL database to be ready
/usr/local/bin/scripts/wait-for-it.sh db:5432 --timeout=60 --strict -- echo "Database is up"

# Optionally wait for Redis if needed
# /usr/local/bin/scripts/wait-for-it.sh redis:6379 --timeout=60 --strict -- echo "Redis is up"

# Start Django server
exec "$@"
