FROM ubuntu:14.04
MAINTAINER Xu,Xin <xinxu1@ebay.com>

RUN apt-get update

#Utilities
RUN apt-get install -y vim less net-tools inetutils-ping curl git telnet nmap socat dnsutils netcat tree htop unzip sudo software-properties-common

#Install Oracle Java 7
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' > /etc/apt/sources.list.d/java.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java7-installer

# Maven
RUN wget -q -O - http://archive.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz | tar -xzf - -C /usr/local \
      && ln -s /usr/local/apache-maven-3.2.5 /usr/local/apache-maven \
      && ln -s /usr/local/apache-maven/bin/mvn /usr/local/bin/mvn

# Pre-cache Druid dependencies 
RUN mvn dependency:get -Dartifact=io.druid:druid-services:0.7.3

#Install Druid
RUN curl http://static.druid.io/artifacts/releases/druid-0.7.3-bin.tar.gz | tar xz
RUN mv druid-0.7.3 druid-services



#MySQL
RUN apt-get install -y mysql-server && \
    sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mysql/my.cnf


# Druid Config
ADD config druid-services/config

#Init MySql
ADD ./mysql.ddl mysql.ddl
RUN mysqld_safe & mysqladmin --wait=5 ping && \
    mysql < mysql.ddl && \
    mysqladmin shutdown

# Pull dependencies for Druid extensions
WORKDIR /druid-services
RUN java -classpath "config/_common:lib/*" io.druid.cli.Main tools pull-deps

# RUN Druid
ADD start.sh /druid-services/start.sh
RUN chmod a+x start.sh
ENTRYPOINT ./start.sh



VOLUME ["/tmp/"]











