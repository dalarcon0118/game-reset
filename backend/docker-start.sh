#!/bin/bash

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
  echo "Docker is not running. Please start Docker and try again."
  exit 1
fi

# Start containers in detached mode using docker-compose.dev.yml
echo "Starting containers using docker-compose.dev.yml..."
docker-compose -f docker-compose.dev.yml up -d --build

# Wait a moment for services to be ready
echo "Waiting for services to start..."
sleep 15

# Create migrations for all apps if they don't exist
echo "Making migrations for all apps..."
docker-compose -f docker-compose.dev.yml exec -T web python manage.py makemigrations

# Run standard Django migrations (this will run all app migrations)
echo "Running migrations..."
docker-compose -f docker-compose.dev.yml exec -T web python manage.py migrate

# Create a superuser
echo "Creating superuser..."
docker-compose -f docker-compose.dev.yml exec -T web python manage.py createsuperuser --noinput --username "${DJANGO_ADMIN_USER:-admin}" --email "${DJANGO_ADMIN_EMAIL:-admin@example.com}"
# Nota: El comando createsuperuser --noinput requiere que las variables de entorno DJANGO_SUPERUSER_PASSWORD, DJANGO_SUPERUSER_USERNAME, y DJANGO_SUPERUSER_EMAIL estén seteadas,
# o puedes quitar --noinput para que te las pida interactivamente.
# Si prefieres el método con shell que tenías antes (adaptado):
docker-compose -f docker-compose.dev.yml exec -T web python manage.py shell -c "
from django.contrib.auth import get_user_model

User = get_user_model()
username = '${DJANGO_ADMIN_USER:-admin}'
email = '${DJANGO_ADMIN_EMAIL:-admin@example.com}'
password = '${DJANGO_ADMIN_PASSWORD:-admin}' # Asegúrate que esta variable esté disponible

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser {username} created successfully.')
else:
    print(f'Superuser {username} already exists.')
"

echo "Startup script finished."
