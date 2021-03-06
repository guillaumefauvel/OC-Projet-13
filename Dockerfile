FROM python:3
ENV PYTHONUNBUFFERED 1
ENV SENTRY_DSN $SENTRY_DSN
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD python3 manage.py runserver 0.0.0.0:8000
EXPOSE 8000