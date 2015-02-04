#
# Docker file for zookeeper
# Create a single node zookeeper server and expose 2181 port.
#

FROM java:openjdk-7-jdk

MAINTAINER  Xinglang Wang <wangxinglang@gmail.com>

# Install zookeeper and do basic configuration.
RUN wget -q -O - http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz | tar -xzf - -C /opt \
    && mv /opt/zookeeper-3.4.6 /opt/zookeeper \
    && cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \
    && mkdir -p /tmp/zookeeper

EXPOSE 2181

WORKDIR /opt/zookeeper
ENTRYPOINT ["/opt/zookeeper/bin/zkServer.sh"]
CMD ["start-foreground"]
