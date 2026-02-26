#!/bin/bash
set -e
source .env

echo "Running database migrations..."
uv run alembic upgrade head
if [ $? -ne 0 ]; then
    echo "Migration failed. Exiting."
    exit 1
fi
echo "Migrations completed successfully."

echo "Starting application..."
exec uv run uvicorn src.main:app --host 0.0.0.0 --port $APP_PORT