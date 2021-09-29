FROM python:3.9.7-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip3 install -r requirements.txt

#If you don't define gunicorn in requirements.txt then
#RUN pip3 install gunicorn

COPY . .

EXPOSE 5000

CMD [ "gunicorn", "--bind" , "0.0.0.0:5000", "app:app"]