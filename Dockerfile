# Container image that runs your code
FROM python:3.10

ENV PYTHONUNBUFFERED=1

COPY sast.py /sast.py

RUN chmod +x sast.py

ENTRYPOINT ["/sast.py"]

