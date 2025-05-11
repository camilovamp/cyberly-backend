#!/bin/sh

echo "⏳ Waiting for MySQL at $DB_HOST..."

while ! nc -z "$DB_HOST" 3306; do
  sleep 1
done

echo "✅ MySQL is up - continuing..."

exec "$@"
