FROM maven:3.2.5-jdk-7

MAINTAINER Xinglang Wang <wangxinglang@gmail.com>

# Set default encoding to UTF-8
RUN echo "LANG=C.UTF-8" > /etc/default/locale

# Build
RUN mkdir -p /opt/app
WORKDIR /opt/app

ENV project_version 4.1.0
ENV project_name configuration

RUN wget http://repo1.maven.org/maven2/com/ebay/jetstream/${project_name}/${project_version}/${project_name}-${project_version}-bin.tar.gz

RUN tar -zxvf ${project_name}-${project_version}-bin.tar.gz
RUN ln -s /opt/app/${project_name}-${project_version} jetstreamapp
WORKDIR /opt/app/jetstreamapp

# App config
ENV JETSTREAM_APP_JAR_NAME ${project_name}.jar
ENV JETSTREAM_APP_NAME ${project_name}
ENV JETSTREAM_CONFIG_VERSION 1.0

# Dependency
ENV JETSTREAM_ZKSERVER_HOST zkserver
ENV JETSTREAM_ZKSERVER_PORT 2181
ENV JETSTREAM_MONGOURL mongo://mongoserver:27017/config

# One http port, no contenxt port
ENV JETSTREAM_REST_BASEPORT 8080
ENV JETSTREAM_APP_PORT 9999

EXPOSE 9999 8080
ENTRYPOINT ./start.sh
