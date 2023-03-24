FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

COPY . .

#CMD ["./sast.py"]
ENTRYPOINT ["/sast.py"]
