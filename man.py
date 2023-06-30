from kafka import KafkaProducer, KafkaConsumer

# Kafka 프로듀서 생성
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# 토픽에 메시지 전송
producer.send('my_topic', b'Hello, Kafka!')

# Kafka 컨슈머 생성
consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092', group_id='my_group')

# 메시지 수신
for message in consumer:
    print(message.value.decode('utf-8'))

