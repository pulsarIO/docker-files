[
    {
        "dataSchema": {
            "dataSource": "pulsar_event",
            "parser": {
                "type": "string",
                "parseSpec": {
                    "format": "json",
                    "timestampSpec": {
                        "column": "ct",
                        "format": "millis"
                    },
                    "dimensionsSpec": {
                        "dimensions": [],
                        "dimensionExclusions": [
                            "guid",
                            "uid",
                            "js_evt_kafka_produce_ts",
                            "timestamp",
                            "js_ev_type"
                        ]
                    }
                }
            },
            "metricsSpec": [
                {
                    "type": "count",
                    "name": "count"
                },
                {
                    "type": "hyperUnique",
                    "name": "guid_hll",
                    "fieldName": "guid"
                },
                {
                    "type": "longSum",
                    "name": "dwell_ag",
                    "fieldName": "dwell"
                }
            ],
            "granularitySpec": {
                "type": "uniform",
                "segmentGranularity": "HOUR",
                "queryGranularity": "NONE"
            }
        },
        "ioConfig": {
            "type": "realtime",
            "firehose": {
                "type": "kafka-0.8",
                "consumerProps": {
                    "zookeeper.connect": "pulsarioZookeeper:2181",
                    "zookeeper.connection.timeout.ms": "30000",
                    "zookeeper.session.timeout.ms": "30000",
                    "zookeeper.sync.time.ms": "5000",
                    "group.id": "docker",
                    "fetch.message.max.bytes": "1048586",
                    "auto.offset.reset": "largest",
                    "auto.commit.enable": "false"
                },
                "feed": "Pulsar.event"
            },
            "plumber": {
                "type": "realtime"
            }
        },
        "tuningConfig": {
            "type": "realtime",
            "maxRowsInMemory": 500000,
            "intermediatePersistPeriod": "PT10m",
            "windowPeriod": "PT10m",
            "basePersistDirectory": "/tmp/druidrealtime/basepersist",
            "rejectionPolicy": {
                "type": "messageTime"
            }
        }
    },
	{
        "dataSchema": {
            "dataSource": "pulsar_session",
            "parser": {
                "type": "string",
                "parseSpec": {
                    "format": "json",
                    "timestampSpec": {
                        "column": "_snet",
                        "format": "millis"
                    },
                    "dimensionsSpec": {
                        "dimensions": [],
                        "dimensionExclusions": [
                            "_snst",
                            "_lon",
			    "_lat",
                            "js_ev_mak",
                            "_snet",
                            "js_ev_type",
			    "_snec"
                        ]
                    }
                }
            },
            "metricsSpec": [
                {
                    "type": "count",
                    "name": "count"
                },
                {
                    "type": "longSum",
                    "name": "totalclick",
                    "fieldName": "_snec"
                },
                {
                    "type": "longSum",
                    "name": "sessionduration_ag",
                    "fieldName": "_sndn"
                }
            ],
            "granularitySpec": {
                "type": "uniform",
                "segmentGranularity": "HOUR",
                "queryGranularity": "NONE"
            }
        },
        "ioConfig": {
            "type": "realtime",
            "firehose": {
                "type": "kafka-0.8",
                "consumerProps": {
                    "zookeeper.connect": "pulsarioZookeeper:2181",
                    "zookeeper.connection.timeout.ms": "30000",
                    "zookeeper.session.timeout.ms": "30000",
                    "zookeeper.sync.time.ms": "5000",
                    "group.id": "docker",
                    "fetch.message.max.bytes": "1048586",
                    "auto.offset.reset": "largest",
                    "auto.commit.enable": "false"
                },
                "feed": "Pulsar.sess"
            },
            "plumber": {
                "type": "realtime"
            }
        },
        "tuningConfig": {
            "type": "realtime",
            "maxRowsInMemory": 500000,
            "intermediatePersistPeriod": "PT10m",
            "windowPeriod": "PT10m",
            "basePersistDirectory": "/tmp/druidrealtime/basepersist",
            "rejectionPolicy": {
                "type": "messageTime"
            }
        }
    }
]
