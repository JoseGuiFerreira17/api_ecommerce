#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then

    while ! nc -z $DB_HOST $DB_PORT; do
        echo "Waiting for postgres..."
        sleep 0.1
    done

    echo "PostgreSQL started"
    
    if [ "$DJANGO_MIGRATE" = "True" ]
    then
        echo "Migrating..."
        python manage.py migrate
    fi
    
    if [ "$DJANGO_COLLECTSTATIC" = "True" ]
    then
        echo "Collecting static files..."
        python manage.py collectstatic --noinput
    fi

    if [ "$DJANGO_ADD_SUPERUSER" = "True" ]
    then
        echo "Creating superuser..."
        python manage.py createsuperuser --name $DJANGO_SUPERUSER_NAME --email $DJANGO_SUPERUSER_EMAIL --noinput
    fi

fi

exec "$@"
