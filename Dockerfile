FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.deno/bin:${PATH}"

RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    curl \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deno.land/install.sh | sh

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -U "yt-dlp[default]" \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/downloads

CMD ["bash", "start"]
