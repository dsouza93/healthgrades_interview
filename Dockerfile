FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV LISTEN_PORT 3000

EXPOSE 3000

COPY ./app /app
