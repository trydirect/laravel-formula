ARG PHP_VERSION=7.4

FROM php:${PHP_VERSION}-fpm

LABEL maintainer="spilchin.serghei@gmail.com"

ADD https://raw.githubusercontent.com/mlocati/docker-php-extension-installer/master/install-php-extensions /usr/local/bin/

RUN chmod uga+x /usr/local/bin/install-php-extensions && sync && \
    install-php-extensions apcu bcmath mbstring tidy curl gd intl pcntl mcrypt pdo_mysql soap xml zip imagick opcache sockets exif

# Install dependencies
RUN apt-get update \
        && apt-get install -y --no-install-recommends \
            build-essential \
            mariadb-client\
            libpng-dev \
            libjpeg62-turbo-dev \
            libfreetype6-dev \
            locales \
            curl \
            supervisor \
            git \
            vim \
            python-setuptools \
            python-pip \
            librabbitmq-dev \
            software-properties-common \
        && apt-get clean \
        && rm -rf \
            ./var/lib/apt/lists/*

RUN pecl install php-amqplib amqp xdebug
RUN docker-php-ext-enable amqp xdebug

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# Download xdebug and install
RUN curl -LO http://xdebug.org/files/xdebug-2.9.6.tgz
RUN tar -xzf xdebug-2.9.6.tgz
RUN cd xdebug-2.9.6 \
    && phpize \
    && ./configure --enable-xdebug \
    && make \
    && make install \
    && cp modules/xdebug.so /usr/local/lib/php/extensions/no-debug-non-zts-20170718 \
    && echo 'zend_extension = /usr/local/lib/php/extensions/no-debug-non-zts-20170718/xdebug.so' >> /usr/local/etc/php.ini \
    && echo 'xdebug.remote_enable=on' >> /usr/local/etc/php.ini \
    && echo 'xdebug.remote_connect_back=1' >> /usr/local/etc/php.ini \
    && echo 'xdebug.remote_host=0.0.0.0' >> /usr/local/etc/php.ini \
    && echo 'xdebug.remote_port=9000' >> /usr/local/etc/php.ini \
    && echo 'xdebug.remote_handler=dbgp' >> /usr/local/etc/php.ini \
    && echo 'xdebug.max_nesting_level=512' >> /usr/local/etc/php.ini \
    && echo 'extension=xdebug.so' >> /usr/local/etc/php.ini

WORKDIR /var/www

ARG LARAVEL_VERSION=7.6.0

RUN git clone -b v${LARAVEL_VERSION} https://github.com/laravel/laravel.git backend
RUN cd backend && composer install

ADD ./configs/php/www.conf /usr/local/etc/php-fpm.d/www.conf
ADD ./configs/supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/supervisor
RUN pip install supervisor