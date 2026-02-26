FROM python:3.13-slim

WORKDIR /app
ARG APP_PORT
RUN apt-get update && apt-get install -y --no-install-recommends curl bash && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir uv
COPY pyproject.toml README.md ./
RUN uv sync --no-dev

COPY . .
RUN chmod +x entrypoint.sh
ENV PYTHONPATH=/src
EXPOSE $APP_PORT
# CMD ["./entrypoint.sh"]
# CMD ["tail", "-f", "/dev/null"]
CMD ["bash", "./entrypoint.sh"]