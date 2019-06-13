FROM php:7.0-apache

RUN groupadd -r -g 2000 bitrix; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/bitrix -s /bin/bash bitrix
RUN apt-get -qq update && apt-get --no-install-recommends -qq install -y locales \
    libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng-dev gettext supervisor curl \
    && apt-get clean; apt-get autoclean; apt-get autoremove -y -qq ;rm -r /var/lib/apt/lists/*

COPY locale.gen /etc/locale.gen
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install -j$(nproc) gd mysqli mcrypt pdo pdo_mysql mbstring tokenizer iconv
RUN a2enmod rewrite
RUN usermod -a -G bitrix www-data

COPY php/php.ini /usr/local/etc/php/conf.d/
COPY encoding.conf /etc/apache2/conf-enabled/encoding.conf
COPY apache2/bitrix.conf /etc/apache2/sites-enabled/000-default.conf
COPY supervisord/apache.conf /etc/supervisor/conf.d/apache.conf
COPY cron/bitrix /etc/crontab

RUN curl -o /usr/src/app.tar.gz -L http://www.bitrixsoft.com/download/portal/en_bitrix24_encode.tar.gz
WORKDIR /var/www/html
RUN tar -xf /usr/src/app.tar.gz
RUN chown -R bitrix.bitrix /var/www/html && chmod g+w -R /var/www/html

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]

