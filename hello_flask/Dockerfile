FROM python:3.8-slim AS build

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir flask mysqlclient

COPY . .

FROM python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libmariadb3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --from=build /opt/venv /opt/venv
COPY --from=build /app /app
ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 5002
CMD ["python", "app.py"]