FROM nikolaik/python-nodejs:python3.10-nodejs20

# FFmpeg extraction ke liye xz-utils aur zaroori tools install karna
RUN apt-get update && apt-get install -y \
    xz-utils \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# FFmpeg download aur setup
RUN curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz \
    -o ffmpeg.tar.xz && \
    tar -xJf ffmpeg.tar.xz && \
    mv ffmpeg-*-static/ffmpeg /usr/local/bin/ && \
    mv ffmpeg-*-static/ffprobe /usr/local/bin/ && \
    rm -rf ffmpeg*

COPY . /app/
WORKDIR /app/

# Windows line endings fix karne ke liye (agar start script mein ho toh)
RUN sed -i -e 's/\r$//' start

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["bash", "start"]
