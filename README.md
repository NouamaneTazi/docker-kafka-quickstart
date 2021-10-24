# Docker Kafka Quickstart

A minimal configuration for a dockerized kafka project.


## Usage:
* Run this command to build `kafka` and `zookeeper` containers, and create the network `kafka-network`, where your containers can access the endpoint `kafka:29092`.
```bash
# creates the network `kafka-network` and build and
# runs the containers for zookeeper and kafka
docker-compose -f "docker-compose.kafka.yml" up -d --build # remove -d if you want to see logs in the same shell
```

* You can then run as many broker/consumer containers on your `kafka-network`, in this case: `generator` is a broker, and `indicator` is a consumer.
```bash
# runs the generator and indicator containers
docker-compose up -d --build
```

* If you check the logs in your `generator` container you should be seeing the messages sent to the `queuing.sentences.test` topic:
```
### KAFKA_BROKER_URL kafka:29092
09:35:09.135969 {'time': '09:35:08.107419', 'player': 'player2', 'sentence': 'sDZRJk nwENFG I sR VOOZNWll aGDdZV'}
09:35:10.138498 {'time': '09:35:10.138207', 'player': 'player2', 'sentence': 'vgIXxE  sa'}
09:35:11.141023 {'time': '09:35:11.140690', 'player': 'player1', 'sentence': 'E raH jzIeKHqXZF JGGB   tx  M oLusi '}
09:35:12.142630 {'time': '09:35:12.142360', 'player': 'player2', 'sentence': 'WxsPlteC  yxh  ogME dvbtFn l b TxVB  gaMFZe'}
09:35:13.144693 {'time': '09:35:13.144454', 'player': 'player1', 'sentence': ' aIRVm W TeIcKuigy  HPLOvJrQSXSl ZlLHlL FRH'}
09:35:14.146182 {'time': '09:35:14.145966', 'player': 'player1', 'sentence': 'cmMH k phZ LapRdGv C geTDzIT'}
09:35:15.147609 {'time': '09:35:15.147378', 'player': 'player2', 'sentence': 'QihJPzjFM WmkmDzMLl DkyydRVeyEI Rm'}
09:35:16.149716 {'time': '09:35:16.149502', 'player': 'player1', 'sentence': '  C '}
09:35:17.151371 {'time': '09:35:17.151155', 'player': 'player2', 'sentence': ''}
09:35:18.152736 {'time': '09:35:18.152508', 'player': 'player1', 'sentence': 'Oh tgfSl tY iBrxMHf aNX h'}
...
```
* And the logs for `indicator` show the messages recieved on the `queuing.sentences.test` topic:
```
### KAFKA_BROKER_URL kafka:29092
Connecting...
Connected to queuing.sentences.test topic!
09:35:13.320414 {'time': '09:35:13.144454', 'player': 'player1', 'sentence': ' aIRVm W TeIcKuigy  HPLOvJrQSXSl ZlLHlL FRH'}
09:35:14.150851 {'time': '09:35:14.145966', 'player': 'player1', 'sentence': 'cmMH k phZ LapRdGv C geTDzIT'}
09:35:15.279800 {'time': '09:35:15.147378', 'player': 'player2', 'sentence': 'QihJPzjFM WmkmDzMLl DkyydRVeyEI Rm'}
09:35:16.153846 {'time': '09:35:16.149502', 'player': 'player1', 'sentence': '  C '}
09:35:17.156841 {'time': '09:35:17.151155', 'player': 'player2', 'sentence': ''}
09:35:18.156372 {'time': '09:35:18.152508', 'player': 'player1', 'sentence': 'Oh tgfSl tY iBrxMHf aNX h'}
09:35:19.160985 {'time': '09:35:19.154674', 'player': 'player2', 'sentence': 'qgSAzkUNm  fBQyruw S U   PvLnharO '}
09:35:20.183376 {'time': '09:35:20.157269', 'player': 'player1', 'sentence': 'OlX SW  a gcpXVGHxW'}
```

## Refs:
For more information about using kafka with Docker: https://hub.docker.com/r/wurstmeister/kafka/
