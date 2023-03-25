# Container image that runs your code
FROM python:3.10

COPY sast.py /sast.py

RUN chmod +x sast.py

ENTRYPOINT ["./sast.py"]

