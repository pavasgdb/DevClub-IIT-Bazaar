# These will create the initial database
python manage.py makeigrations
python manage.py migrate

# This will create the superuser
python manage.py createsuperuser

# This will start the server
python manage.py runserver