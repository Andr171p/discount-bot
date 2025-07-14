#!/bin/bash
set -e

# Функция для проверки доступности PostgreSQL
wait_for_postgres() {
    local max_retries=10
    local retry_interval=5

    echo "Waiting for PostgreSQL to become available..."

    for ((i=1; i<=max_retries; i++)); do
        if pg_isready -h db -U ${POSTGRES_USER} -d ${POSTGRES_DB} -t 1; then
            echo "PostgreSQL is ready!"
            return 0
        fi
        echo "Attempt $i/$max_retries: PostgreSQL not ready, waiting $retry_interval seconds..."
        sleep $retry_interval
    done

    echo "Failed to connect to PostgreSQL after $max_retries attempts"
    return 1
}

# Выполняем миграции только при первом запуске
if [ ! -f /app/.db_initialized ]; then
    wait_for_postgres

    echo "Running database migrations..."
    alembic upgrade head

    touch /app/.db_initialized
    echo "Database initialization complete"
fi

# Запускаем основной процесс
exec "$@"