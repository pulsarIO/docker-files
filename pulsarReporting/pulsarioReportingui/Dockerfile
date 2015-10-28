FROM    centos:centos6

# Enable EPEL for Node.js
RUN     rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
# Install Node.js and npm
RUN     yum install -y npm unzip git




WORKDIR /usr/local
RUN git clone -b gh-pages https://github.com/pulsarIO/pulsar-reporting-ui.git
WORKDIR /usr/local/pulsar-reporting-ui
RUN mkdir pulsar-reporting-ui-docker
RUN unzip pulsar-reporting-ui-bundle.zip -d pulsar-reporting-ui-docker/
WORKDIR /usr/local/pulsar-reporting-ui/pulsar-reporting-ui-docker
ADD start.sh /usr/local/pulsar-reporting-ui/pulsar-reporting-ui-docker/start.sh
#sed -i 's/<PULSARIO_TOMCAT>/http:\/\/pulsarioTomcat:8080\/prapi\/v2/g' config-bundle.json

ENTRYPOINT ./start.sh
CMD ./start.sh
