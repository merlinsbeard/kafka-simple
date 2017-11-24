# Kafka Simple

Requirements:

* Python 3.3 ++

Installation:

```shell
$ git@github.com:merlinsbeard/kafka-simple.git
$ cd kafka-simple
$ python3 setup.py install
$ kafsim --help
```

## Produce Message

```shell
$ kafsim --url 128.169.69.9:9002 --topic my-topic produce
```

## Consume Message

```shell
$ kafsim --url 128.169.69.9:9002 --topic my-topic consume
```
