run-dev:
	python manage.py runserver 0.0.0.0:8000
run-prod:
	gunicorn web.wsgi:application --bind 0.0.0.0:8000
migrate:
	python manage.py migrate
collectstatic:
	python manage.py collectstatic --no-input
