FROM python:3.10-alpine

COPY . .

RUN chmod +x sast.py

ENTRYPOINT ["/sast.py"]
