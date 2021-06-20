# family
Test program with python and django

## Running tests
docker-compose run app sh -c "python manage.py test"

## Creating a django app 
docker-compose run app sh -c "python manage.py startapp (name of app)"

## Running migration after modifying models 
add app name if wants to run migration for only specific app
docker-compose run app sh -c "python manage.py makemigrations"

## Running tests and lints before committing
docker-compose run app sh -c "python manage.py test && flake8"