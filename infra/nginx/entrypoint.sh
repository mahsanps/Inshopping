# infra/nginx/entrypoint.sh

#!/bin/bash
set -e

# Wait for Django to be ready
wait-for-it.sh django:8000 --timeout=60 --strict -- echo "Django is up"

# Start Nginx in the foreground
exec nginx -g "daemon off;"
