#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate


# Variables de entorno para el superusuario
SUPERUSER_USERNAME="adrian"
SUPERUSER_EMAIL="penate.adrian01@gmail.com"
SUPERUSER_PASSWORD="123456"

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$SUPERUSER_USERNAME', '$SUPERUSER_EMAIL', '$SUPERUSER_PASSWORD')" | python manage.py shell
