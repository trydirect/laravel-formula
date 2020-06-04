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

- PHP 7.4-fpm docker image,
- Laravel 7.6.0
- Xdebug 2.9.6
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
$ cd laravel-formula/7.6.0
$ docker-compose up -d
```
Let's finish setup with configuring stack
```
cp backend/.env.example backend/.env

docker-compose exec web bash -c "composer install"

docker-compose exec web bash -c "chmod -R 777 /var/www/backend/storage/"

docker-compose exec web bash -c "php artisan key:generate"
```

Let's check running containers

```
 $ docker-compose ps

IMAGE                         COMMAND              CREATED         STATUS              PORTS 
kibana:5.4.3            "/docker-entrypoint.…"   2 hours ago         Up         0.0.0.0:5601->5601/tcp
logstash                "/usr/local/bin/dock…"   2 hours ago         Up         9600/tcp, 0.0.0.0:32775->5044/tcp
nginx:latest            "/docker-entrypoint.…"   2 hours ago         Up         0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp
elasticsearch           "/docker-entrypoint.…"   2 hours ago         Up         9200/tcp, 9300/tcp
laravel:7.6.0           "/usr/local/bin/supe…"   2 hours ago         Up         9000/tcp
rabbitmq:3-management   "docker-entrypoint.s…"   2 hours ago         Up         4369/tcp, 5671/tcp, 15671-15672/tcp, 25672/tcp, 0.0.0.0:5672->5672/tcp, 0.0.0.0:32774->21072/tcp
mysql:5.7               "docker-entrypoint.s…"   2 hours ago         Up         3306/tcp, 33060/tcp
redis:latest            "docker-entrypoint.s…"   2 hours ago         Up         6379/tcp       
```

Find examples in laravel-formula/7.6.0/backend:                 
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
[<img src="https://img.shields.io/badge/quick%20deploy-%40try.direct-brightgreen.svg">](https://dev.try.direct/server/user/deploy/ImxhcmF2ZWwtZm9ybXVsYXw2fDIi.EAoFeA.nBrVq7PjzFGucxAw44D1Sf9J7ws/)



# Contributing

1. Fork it (https://github.com/trydirect/laravel-formula/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request



# Support Development

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2BH8ED2AUU2RL)
