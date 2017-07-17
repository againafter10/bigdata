

#######################################
# Kafka Producer
#######################################
import random,string
from kafka import KafkaProducer
from kafka.errors import KafkaError

# kafka-console-producer --broker-list 127.0.0.1:9092 --topic WARN
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


# Asynchronous by default
# kafka topic is "LOGWARN"
future = producer.send('LOGWARN', b'raw_bytes')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)

'''
# produce keyed messages to enable hashed partitioning
producer.send('WARN', key=b'foo', value=b'bar')

# encode objects via msgpack
producer = KafkaProducer(value_serializer=msgpack.dumps)
producer.send('msgpack-topic', {'key': 'value'})

# produce json messages
producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
producer.send('json-topic', {'key': 'value'})

# produce asynchronously
for _ in range(100):
    producer.send('WARN', b'msg')
'''

# produce asynchronously
chars=string.ascii_uppercase + string.digits
while True:
    str=''.join(random.choice(chars) for _ in range(10))
    producer.send('LOGWARN', str)



# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)