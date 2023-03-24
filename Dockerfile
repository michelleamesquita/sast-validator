FROM python:3.10-alpine

# COPY . .

WORKDIR app

COPY sast.py /app/sast.py


RUN chmod +x sast.py

ENTRYPOINT ["python3","sast.py"]
