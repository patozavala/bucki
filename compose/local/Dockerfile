# We will inherit from the python3.8.5 image on DockerHub
FROM python:3.8.5

# Ensures that the python output is sent straight to terminal
ENV PYTHONUNBUFFERED 1

# Set timezone so files' timestamps are correct
ENV TZ=America/Santiago

# Requirements are installed here to ensure they will be cached.
RUN pip install --upgrade pip
COPY ["./requirements", "/requirements"]
RUN pip install -r /requirements/local.txt

COPY ["./compose/local/entrypoint", "/entrypoint"]
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ["./compose/local/start", "/start"]
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app
COPY [".","/app"]

ENTRYPOINT ["/entrypoint"]
