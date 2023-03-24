FROM python:3.10-alpine

# COPY . .

COPY sast.py /sast.py


RUN chmod +x sast.py

ENTRYPOINT ["/sast.py"]
