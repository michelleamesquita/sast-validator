# Container image that runs your code
FROM python:3.6

ENV PYTHONUNBUFFERED=1


# COPY sast.py /sast.py

# RUN chmod +x sast.py

# ENTRYPOINT ["/sast.py"]

RUN mkdir app

COPY sast.py /app/sast.py

COPY entrypoint.sh /entrypoint.sh


RUN chmod +x /app/sast.py
RUN chmod +x /entrypoint.sh



ENTRYPOINT ["/entrypoint.sh"]

# CMD ["-d=.", "-l=python"]



# RUN mkdir app

# COPY sast.py /app/sast.py
# COPY entrypoint.sh /entrypoint.sh

# COPY sast.py /sast.py

# RUN chmod +x /app/sast.py
# RUN chmod +x /entrypoint.sh


# CMD ["-d", ".", "-l", "python"]

# ENTRYPOINT ["sh", "-c", "cd /app && ./sast.py"]

# ENTRYPOINT ./sast.py -d $dir -l $lang

# ENTRYPOINT ./sast.py

# ENTRYPOINT ["sh", "-c", "cd /app && ./sast.py"]

# ENTRYPOINT ["cd /app && && ./sast.py"]

# ENTRYPOINT ["python3", "sast.py"]

# CMD ["-d=.", "-l=python"]

# ENTRYPOINT ["./entrypoint.sh"]

# CMD ["-d=."]