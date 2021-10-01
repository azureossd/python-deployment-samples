FROM python:3.9.7-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip3 install -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations blog \
    && python3 manage.py migrate --noinput 
#To create superuser you might need to exec to the container and create it.
 
#https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/
RUN python3 manage.py collectstatic --noinput 

EXPOSE 8000

CMD [ "gunicorn", "--bind" , "0.0.0.0:8000", "company.wsgi:application"]
