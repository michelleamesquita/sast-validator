FROM python:3.10-alpine

COPY . .

RUN chmod +x sast.py

RUN ls -la

ENTRYPOINT ["/sast.py"]
