FROM ubuntu:14.04
# Java installation.
#
# You have to either start with an image that has Java 7 pre-installed,
# or manually download Java once, host it somewhere, and wget it.
#install Oracle Java 7
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' > /etc/apt/sources.list.d/java.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java7-installer

# Other stuff can be installed with yum
# (Note that git is quite old. If you want 1.8.x, install from source.)
RUN apt-get update && apt-get install -y git wget tar



# Tomcat 8
#
# Not available on yum, so install manually
RUN wget -O /tmp/apache-tomcat-8.0.28.tar.gz http://apache.mirrors.lucidnetworks.net/tomcat/tomcat-8/v8.0.28/bin/apache-tomcat-8.0.28.tar.gz
RUN cd /usr/local && tar xzf /tmp/apache-tomcat-8.0.28.tar.gz
RUN ln -s /usr/local/apache-tomcat-8.0.28 /usr/local/tomcat
RUN rm /tmp/apache-tomcat-8.0.28.tar.gz


# Maven
RUN wget -q -O - http://archive.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz | tar -xzf - -C /usr/local \
      && ln -s /usr/local/apache-maven-3.2.5 /usr/local/apache-maven \
      && ln -s /usr/local/apache-maven/bin/mvn /usr/local/bin/mvn

# Clone the application itself
WORKDIR /usr/local/tomcat



RUN rm -rf /usr/local/tomcat/webapps
RUN mkdir /usr/local/tomcat/webapps

RUN git clone https://github.com/pulsarIO/pulsar-reporting-api.git
WORKDIR /usr/local/tomcat/pulsar-reporting-api
# Copy start script
ADD start.sh /usr/local/tomcat/pulsar-reporting-api/start.sh
RUN chmod a+x start.sh

RUN mvn clean install package -Dmaven.test.skip=true
RUN cp pulsarquery-service/target/ROOT.war /usr/local/tomcat/webapps
ADD pulsar-config.properties /root/pulsar-config.properties

# Environment variables
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/
ENV CATALINA_HOME /usr/local/tomcat
ENV APP_HOME /usr/local/prapi


ENTRYPOINT ./start.sh
CMD ./start.sh

# Forward HTTP ports
EXPOSE 80 8080
                                     
