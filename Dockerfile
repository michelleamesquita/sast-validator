FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

COPY . .

RUN chmod +x sast.py

#CMD ["./sast.py"]
ENTRYPOINT ["./sast.py"]
