import fire
from kafka import KafkaConsumer, KafkaProducer
import logging as logger


logger.basicConfig(level=logger.INFO)


class Hello():
    def __init__(self,
                 url="127.0.0.1:9092",
                 topic="hello"):
        self.url = url
        self.topic = topic
        message = 'URL: {}, TOPIC: {}'.format(self.url, self.topic)
        logger.info(message)

    def consume(self):
        logger.info("Starting Consumer")
        try:
            consumer = KafkaConsumer(self.topic, bootstrap_servers=self.url)
            logger.info("Connected")
            for msg in consumer:
                logger.info("CON CON CON ")
                print(msg)

        except Exception as e:
            logger.error(e)
            logger.error("FAILED")


    def produce(self, message="HOLAAAAAAAAAAAA"):
        logger.info("Starting Producer")
        try:
            producer = KafkaProducer(bootstrap_servers=self.url)
            logger.info(producer)
            logger.info("Producer connecter")
        except:
            logger.error("Kafka Producer Failed")

        try:
            producer.send(self.topic, message)
            logger.info("Sending message")
            producer.flush
        except:
            logger.error("Message Sending Failed")
        logger.info("FLUSHED")


def main():
    fire.Fire(Hello)


if __name__ == '__main__':
    fire.Fire(Hello)
