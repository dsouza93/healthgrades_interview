FROM python:3.6 

EXPOSE 3000

COPY . ./interview_api

WORKDIR /interview_api

RUN pip install Flask

ENTRYPOINT ["python", "interview_api/main.py"]
