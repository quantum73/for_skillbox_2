#!/bin/sh

echo "Waiting for postgres..."

set -e

host="db"
shift

until PGPASSWORD="postgres" psql -h "$host" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "PostgreSQL started"

python manage.py makemigrations
python manage.py migrate
exec "$@"
