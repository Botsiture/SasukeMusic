FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive PYTHONUNBUFFERED=1 PATH="/root/.deno/bin:${PATH}"
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg git curl unzip ca-certificates && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://deno.land/install.sh | sh
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /app/
RUN mkdir -p /app/downloads

EXPOSE 8080

CMD ["bash", "start"]
