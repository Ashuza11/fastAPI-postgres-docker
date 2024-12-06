#!/bin/bash
set -e

# Wait for PostgreSQL to be ready
until psql -h "$DB_HOST" -U "$POSTGRES_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

# Run the database initialization commands
psql -h "$DB_HOST" -U "$POSTGRES_USER" -c "CREATE DATABASE $POSTGRES_DB;"
psql -h "$DB_HOST" -U "$POSTGRES_USER" -c "CREATE USER $POSTGRES_USER WITH ENCRYPTED PASSWORD '$POSTGRES_PASSWORD';"
psql -h "$DB_HOST" -U "$POSTGRES_USER" -c "GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;"

# Execute the command passed to the container
exec "$@"