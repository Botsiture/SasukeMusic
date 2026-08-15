FROM nikolaik/python-nodejs:python3.10-nodejs20

# System par direct FFmpeg aur zaroori tools install karna (No errors)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["bash", "start"]
