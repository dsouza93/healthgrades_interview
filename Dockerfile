FROM python:3.6 

EXPOSE 3000

COPY . ./app

WORKDIR /app

RUN pip install Flask

ENTRYPOINT ["python"]
CMD ["app/main.py"]
