FROM python:3.10-alpine

COPY . .

ENTRYPOINT ["/sast.py "]
