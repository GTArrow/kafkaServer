from kafka import KafkaProducer
import requests
import json
import time

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    api_version=(0,11,5),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to fetch data from API and send to Kafka
def fetch_and_send():
    print("Fetching data:")
    response = requests.get("https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=t0Nm6euS13XNzB57Mrl49DI4rHVwU5Kt")
    if response.status_code == 200:
        hourly_data = []
        print("Flushing data:")
        data = response.json()  # Assuming JSON response
        latitude = data["location"]["lat"]
        longitude = data["location"]["lon"]
        for item in data["timelines"]["hourly"]:
            data_point = {
                "time": item["time"],
                "lat": latitude,
                "lon": longitude,
                **item["values"]  # Merge all values into the dictionary
            }
            producer.send('testing_data', value=data_point)
            producer.flush()  # Flush after each send to ensure delivery
            print(f"Sent: {item}")

# Periodically call the function
while(True):
    fetch_and_send()
    time.sleep(10)
