FROM python:3.10

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "nombre_proyecto.wsgi:application"]
