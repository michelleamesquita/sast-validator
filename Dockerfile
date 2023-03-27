# Container image that runs your code
FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY sast.py /app/sast.py

RUN chmod +x sast.py


ENTRYPOINT ["./sast.py"]

CMD ["-d=.", "-l=python"]