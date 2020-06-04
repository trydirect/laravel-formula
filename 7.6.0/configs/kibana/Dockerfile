FROM kibana:5.4.3

RUN kibana-plugin install x-pack
COPY kibana.yml /usr/share/kibana/config
RUN chown kibana:kibana -R  /usr/share/kibana/optimize/bundles