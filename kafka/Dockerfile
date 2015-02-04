#
# Docker file for zookeeper
# Create a single node zookeeper server and expose 2181 port.
#

FROM java:openjdk-7-jdk

MAINTAINER  Xinglang Wang <wangxinglang@gmail.com>

# Install zookeeper and do basic configuration
RUN wget -q -O - http://mirror.gopotato.co.uk/apache/kafka/0.8.1.1/kafka_2.8.0-0.8.1.1.tgz | tar -xzf - -C /opt \
    && mv /opt/kafka_2.8.0-0.8.1.1 /opt/kafka 
        && mkdir /kafka

ENV KAFKA_HOME /opt/kafka
WORKDIR /opt/kafka
EXPOSE 2181 9092

RUN echo "#!/bin/sh" >> start.sh
RUN echo "SERVERIP=\`ip -f inet addr show eth0 | grep inet | awk '{print \$2}' | cut -f1  -d'/'\`" >> start.sh
RUN echo "sed \"s/#host.name=localhost/host.name=\$SERVERIP/\" config/server.properties > config/server.properties.1" >> start.sh
RUN echo "bin/zookeeper-server-start.sh -daemon config/zookeeper.properties" >> start.sh
RUN echo "bin/kafka-server-start.sh config/server.properties.1" >> start.sh
RUN chmod +x start.sh

ENTRYPOINT ./start.sh