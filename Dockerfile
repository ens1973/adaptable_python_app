FROM python:3.9-alpine
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV PYTHONUNBUFFERED 1
EXPOSE 5000

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apk add gcc musl-dev libffi-dev openssl-dev build-base
RUN pip install -r requirements.txt
COPY . /code/

# CMD flask run
CMD python main.py
#CMD python manage.py run
#CMD gunicorn --bind 0.0.0.0:5000 -w 3 --timeout 300 --access-logfile ../logs/app1_logs.log run:app