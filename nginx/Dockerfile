FROM nginx:1.14

COPY conf/nginx.conf /etc/nginx/
COPY conf/default.conf /etc/nginx/conf.d/
COPY conf/upstream.conf /etc/nginx/conf.d/
COPY conf/push_and_pull.conf /etc/nginx/conf.d/

RUN apt-get update && apt-get install apt-file -y && apt-file update && apt-get install vim git wget curl net-tools build-essential gcc make libpcre++-dev zlib1g-dev libssl-dev -y
RUN git clone https://github.com/wandenberg/nginx-push-stream-module.git
ENV NGINX_PUSH_STREAM_MODULE_PATH=$PWD/nginx-push-stream-module
RUN wget http://nginx.org/download/nginx-1.2.0.tar.gz && tar xzvf nginx-1.2.0.tar.gz
WORKDIR nginx-1.2.0
RUN wget http://zlib.net/zlib-1.2.11.tar.gz && tar -xf zlib-1.2.11.tar.gz
RUN wget https://www.openssl.org/source/openssl-1.0.2n.tar.gz && tar -xf openssl-1.0.2n.tar.gz
RUN wget https://ftp.pcre.org/pub/pcre/pcre-8.41.tar.gz && tar -xf pcre-8.41.tar.gz
RUN ./configure --add-module=../nginx-push-stream-module --with-zlib=./zlib-1.2.11 --with-openssl=./openssl-1.0.2n --with-pcre=./pcre-8.41 --with-http_ssl_module && make build && make install

RUN mv /usr/sbin/nginx /usr/sbin/nginx_backup
RUN mv /usr/local/nginx/sbin/nginx /usr/sbin/nginx

RUN mv /usr/local/nginx/conf/ /usr/local/nginx/conf_del
RUN ln -s /etc/nginx/ /usr/local/nginx/conf

COPY conf/init-deb.sh /etc/init.d/
RUN mv /etc/init.d/init-deb.sh /etc/init.d/nginx
RUN chmod +x /etc/init.d/nginx
RUN /usr/sbin/update-rc.d -f nginx defaults

RUN usermod -u 1000 www-data

CMD ["nginx"]

EXPOSE 80 443 8893 8894 8895
