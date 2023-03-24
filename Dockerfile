FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

RUN pip install -U pip

COPY sast.py .

RUN chmod +x sast.py

ENTRYPOINT ["./sast.py"]
