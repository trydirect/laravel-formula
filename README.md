[![Build Status](https://travis-ci.com/trydirect/laravel-formula.svg?branch=master)](https://travis-ci.com/trydirect/laravel-formula)
![Docker Stars](https://img.shields.io/docker/stars/trydirect/laravel.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/trydirect/laravel.svg)
![Docker Automated](https://img.shields.io/docker/cloud/automated/trydirect/laravel.svg)
![Docker Build](https://img.shields.io/docker/cloud/build/trydirect/laravel.svg)
[![Gitter chat](https://badges.gitter.im/trydirect/community.png)](https://gitter.im/try-direct/community)


# Laravel development template.
Laravel development template - project generator/development environment.
Can be used by Laravel developers to start quickly on building web apps, restful api's etc.
This stack allows you to setup development environment with a single docker-compose command

## Stack includes

- PHP7.2/fpm docker image,
- Laravel 5.7
- NGINX latest (tuned with letsencrypt and self signed certificate support)
- MySQL 5.7
- Redis latest
- RabbitMQ 3
- ELK (Logs), Elasticsearch 5.4, Kibana 5.4
- Hashicorp Vault (Credentials management)

## Note
Before installing this project, please, make sure you have installed docker and docker-compose

To install docker execute: 
```sh
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sh get-docker.sh
$ pip install docker-compose
```
## Installation
Clone this project into your work directory:
```sh
$ git clone https://github.com/trydirect/laravel-formula.git
```
Then build it via docker-compose:
```sh
$ cd laravel-formula/5.7
$ docker-compose up -d
```
Let's finish setup with configuring stack
```
cp backend/.env.example backend/.env
docker-compose exec web composer install
```
Now, let's check the result
```
$ curl http://localhost/test

HTTP/1.1 200 OK
Server: nginx/1.15.12
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
X-Powered-By: PHP/7.2.18
Set-Cookie: XDEBUG_SESSION=laravel; expires=Fri, 24-May-2019 17:02:22 GMT; Max-Age=3600; path=/
Cache-Control: no-cache, private
Date: Fri, 24 May 2019 16:02:23 GMT
Set-Cookie: XSRF-TOKEN=eyJpdiI6IlNCNWxlOGdkXC9qa2ZlQUMxTnlpeFdnPT0iLCJ2YWx1ZSI6InZDQzlJM1NvZjhlZW5xZE8rN3ZHVDNDNTFNa0hGK0RRcFhKVDRpTnZVY0tpeWdoUnhXbDJ1Uys1QnpXeFpnQ2QiLCJtYWMiOiI4ZDAwODFmMDBhOTJkZDNhOGRlOGZhYjRmY2ExYzdhMjJjMDMxZmNhMTdjNzQ5Zjc5Zjc1NjI3NWEzZjJiMWJlIn0%3D; expires=Fri, 24-May-2019 18:02:23 GMT; Max-Age=7200; path=/
Set-Cookie: laravel_session=eyJpdiI6IlwvNjZTVHY3MXBcL3hsbWF1a0t0VG1Sdz09IiwidmFsdWUiOiJPKzJvb2dmeG5lSFE1Z2VzSUJaYUQ0NXlwRGxJVUNnd1ZpNlFiV0NPYkZlSW9pV1A1d1NiZmpxYXJJaTFRS2R3IiwibWFjIjoiOTgyMzczMmUxZGNlM2U1OGEzOGI0YTE3YTkwMGIxN2UyNGI5NTUyZjM1MWU0MGNhNzE1ZDk3NjBjNjY2ZDI0YiJ9; expires=Fri, 24-May-2019 18:02:23 GMT; Max-Age=7200; path=/; httponly

Hello World!%
```

Let's check running containers
```

 $ docker-compose ps
 
Name               Command               State                                                   Ports
-------------------------------------------------------------------------------------------------------------------------
db      docker-entrypoint.sh mysqld      Up      3306/tcp, 33060/tcp
mq      docker-entrypoint.sh rabbi ...   Up      15671/tcp, 15672/tcp, 0.0.0.0:32933->21072/tcp, 25672/tcp, 4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp
nginx   nginx -g daemon off;             Up      0.0.0.0:443->443/tcp, 0.0.0.0:80->80/tcp
redis   docker-entrypoint.sh redis ...   Up      6379/tcp
web     /usr/local/bin/supervisord ...   Up      9000/tcp
```

Find examples in laravel-formula/5.7/backend:                 
```
$ tree routes
routes
├── api.php
├── channels.php
├── console.php
└── web.php
```

## Quick deployment to cloud
##### Amazon AWS, Digital Ocean, Hetzner and others
[<img src="https://img.shields.io/badge/quick%20deploy-%40try.direct-brightgreen.svg">](https://try.direct/server/user/deploy/ImxhcmF2ZWwtZm9ybXVsYXw2fDIi.EAoFeA.nBrVq7PjzFGucxAw44D1Sf9J7ws/)



# Contributing

1. Fork it (https://github.com/trydirect/laravel-formula/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request



# Support Development

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2BH8ED2AUU2RL)
