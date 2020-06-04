FROM docker.elastic.co/logstash/logstash:5.4.0

WORKDIR /usr/share/logstash
RUN rm -rf /usr/share/logstash/pipeline/*
COPY ./filebeat.conf /usr/share/logstash/pipeline
COPY ./logstash.yml /usr/share/logstash/config
RUN bin/logstash-plugin install x-pack
RUN logstash-plugin install logstash-filter-json