FROM maven:3.2.5-jdk-7

MAINTAINER Xinglang Wang <wangxinglang@gmail.com>

# Set default encoding to UTF-8
RUN echo "LANG=C.UTF-8" > /etc/default/locale

# Build
RUN mkdir -p /opt/app

WORKDIR /opt
RUN git clone https://github.com/pulsarIO/realtime-analytics.git
WORKDIR /opt/realtime-analytics/
RUN git checkout realtime-analytics-1.0.0
WORKDIR /opt/realtime-analytics/collector
RUN mvn -DskipTests clean install

ENV project_version 1.0.0
ENV project_name collector

RUN cp target/${project_name}-${project_version}-bin.tar.gz /opt/app/${project_name}-${project_version}-bin.tar.gz
WORKDIR /opt/app
RUN tar -zxvf ${project_name}-${project_version}-bin.tar.gz
RUN ln -s /opt/app/${project_name}-${project_version} jetstreamapp
WORKDIR /opt/app/jetstreamapp

# Download and install mmdb.
RUN wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz && gunzip GeoLite2-City.mmdb.gz && mkdir geodb && mv GeoLite2-City.mmdb geodb/

# App config
ENV JETSTREAM_APP_JAR_NAME ${project_name}.jar
ENV JETSTREAM_APP_NAME ${project_name}
ENV JETSTREAM_CONFIG_VERSION 1.0

# Dependency
ENV JETSTREAM_ZKSERVER_HOST zkserver
ENV JETSTREAM_ZKSERVER_PORT 2181
ENV JETSTREAM_MONGOURL mongo://mongoserver:27017/config
ENV PULSAR_KAFKA_BORKERS kafkaserver:9092

EXPOSE 8080 9999 15590
ENTRYPOINT ./start.sh
