FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

COPY sast.py .

RUN chmod +x sast.py

ENTRYPOINT ["./sast.py"]
