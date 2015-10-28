ip=$(getent hosts pulsarioReportingapi | awk '{ print $1 }')
sed -i "s/<pulsarioReportingapi>/${ip}:8080/g" config-bundle.json
node server.dist.js

