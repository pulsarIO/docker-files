FROM maven:3.2.5-jdk-7

MAINTAINER Xinglang Wang <wangxinglang@gmail.com>

# Set default encoding to UTF-8
RUN echo "LANG=C.UTF-8" > /etc/default/locale

# Build
RUN mkdir -p /opt/app
WORKDIR /opt/app

WORKDIR /opt
RUN git clone https://github.com/pulsarIO/jetstream.git
WORKDIR /opt/jetstream/
RUN git checkout jetstream-root-4.0.2
WORKDIR /opt/jetstream/configurationmanagement
RUN mvn -Djettyserver.version=9.2.2.v20140723 -DskipTests clean install

ENV project_version 4.0.2
ENV project_name configuration

RUN cp target/${project_name}-${project_version}-bin.tar.gz /opt/app/${project_name}-${project_version}-bin.tar.gz
WORKDIR /opt/app

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

EXPOSE 9999 8080
ENTRYPOINT ./start.sh
