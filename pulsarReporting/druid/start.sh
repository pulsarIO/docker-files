#!/bin/sh

chown -R mysql:mysql /var/lib/mysql
/usr/bin/mysqld_safe&

exec java -Xmx1g -Duser.timezone=UTC -Dfile.encoding=UTF-8 -Dlogsuffix=coordinator -Djava.util.logging.manager=org.apache.logging.log4j.jul.LogManager -classpath config/coordinator:config/_common:lib/* io.druid.cli.Main server coordinator >/dev/null &


exec java -Xmx512m -Duser.timezone=UTC -Dfile.encoding=UTF-8 -Dlogsuffix=broker -Djava.util.logging.manager=org.apache.logging.log4j.jul.LogManager -classpath config/broker:config/_common:lib/* io.druid.cli.Main server broker >/dev/null &
exec java -Xmx3g -Duser.timezone=UTC -Dfile.encoding=UTF-8 -Dlogsuffix=realtime -Djava.util.logging.manager=org.apache.logging.log4j.jul.LogManager -Ddruid.realtime.specFile=config/realtime/kafka.soj.spec -classpath config/_common:config/realtime:lib/*:/root/.m2/repository/org/apache/hadoop/hadoop-hdfs/2.3.0/hadoop-hdfs-2.3.0.jar:/root/.m2/repository/org/apache/hadoop/hadoop-common/2.3.0/hadoop-common-2.3.0.jar:/root/.m2/repository/org/apache/hadoop/hadoop-client/2.3.0/hadoop-client-2.3.0.jar:/root/.m2/repository/org/apache/hadoop/hadoop-auth/2.3.0/hadoop-auth-2.3.0.jar:/root/.m2/repository/commons-collections/commons-collections/3.2.1/commons-collections-3.2.1.jar:/root/.m2/repository/commons-configuration/commons-configuration/1.6/commons-configuration-1.6.jar io.druid.cli.Main server realtime >/dev/null &

exec java -Xmx3g -Duser.timezone=UTC -Dfile.encoding=UTF-8 -Dlogsuffix=historical -Djava.util.logging.manager=org.apache.logging.log4j.jul.LogManager -classpath config/historical:config/_common:lib/*:/root/.m2/repository/org/apache/hadoop/hadoop-hdfs/2.3.0/hadoop-hdfs-2.3.0.jar:/root/.m2/repository/org/apache/hadoop/hadoop-common/2.3.0/hadoop-common-2.3.0.jar:/root/.m2/repository/org/apache/hadoop/hadoop-client/2.3.0/hadoop-client-2.3.0.jar:/root/.m2/repository/org/apache/hadoop/hadoop-auth/2.3.0/hadoop-auth-2.3.0.jar:/root/.m2/repository/commons-collections/commons-collections/3.2.1/commons-collections-3.2.1.jar:/root/.m2/repository/commons-configuration/commons-configuration/1.6/commons-configuration-1.6.jar io.druid.cli.Main server historical >/dev/null &

exec java -Xmx512m -Duser.timezone=UTC -Dfile.encoding=UTF-8 -Dlogsuffix=overlord -Djava.util.logging.manager=org.apache.logging.log4j.jul.LogManager -classpath config/overlord:config/_common:lib/*: io.druid.cli.Main server overlord >/dev/null
