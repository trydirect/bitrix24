FROM debian:buster-slim

RUN apt-get update && apt-get install -y git wget gcc make libpcre++-dev zlib1g-dev libssl-dev
RUN git clone http://github.com/wandenberg/nginx-push-stream-module.git
ENV NGINX_PUSH_STREAM_MODULE_PATH=$PWD/nginx-push-stream-module
RUN wget http://nginx.org/download/nginx-1.16.1.tar.gz && tar xzvf nginx-1.16.1.tar.gz
WORKDIR nginx-1.16.1
RUN ./configure --add-module=../nginx-push-stream-module && make && make install

CMD ['nginx']


