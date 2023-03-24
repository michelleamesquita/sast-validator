FROM python:3.10-alpine

COPY sast.py .

RUN chmod +x sast.py

ENTRYPOINT ["./sast.py"]
