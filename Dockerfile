# Container image that runs your code
FROM python:3.10

COPY sast.py /sast.py

RUN chmod +x sast.py


# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["./sast.py"]

