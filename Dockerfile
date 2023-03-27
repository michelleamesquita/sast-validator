# Container image that runs your code
FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG dir="."
ARG lang="python"

WORKDIR /app

COPY sast.py /app/sast.py

RUN chmod +x sast.py






# CMD ["-d", ".", "-l", "python"]

#ENTRYPOINT ["sh", "-c", "cd /app && ./sast.py"]

# ENTRYPOINT ./sast.py -d $dir -l $lang

# ENTRYPOINT ./sast.py

ENTRYPOINT ["sh", "-c", "cd /app && ./sast.py"]