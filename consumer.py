from kafka import KafkaConsumer
import json

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'testing_data',                           # Replace with your Kafka topic name
    bootstrap_servers=['localhost:9092'],    # Replace with your MSK or Kafka broker endpoints
    auto_offset_reset='earliest',               # Start reading at the beginning if no offset exists
    enable_auto_commit=True,                    # Automatically commit offsets
    group_id='my-consumer-group1',               # Consumer group ID for load balancing
    value_deserializer=lambda x: json.loads(x.decode('utf-8')), # Decode message to JSON
    api_version=(0,11,5)
)

# Process messages from Kafka
print(f"Pipeline Started:")
try:
    for message in consumer:
        data = message.value
        # Handle the consumed message (print or process data)
        print(f"Received message:")
        # Add any custom processing logic here
        print(json.dumps(data, indent=4))
except KeyboardInterrupt:
    print("Consumer interrupted.")
finally:
    consumer.close()
    print("Consumer connection closed.")
