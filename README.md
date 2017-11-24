# Kafka Simple

Installation:

```shell
$ python setup.py install
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
