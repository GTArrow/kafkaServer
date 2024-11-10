from kafka import KafkaProducer
import requests
import json
import time
import sys
from pathlib import Path

import utils.forest_geo_helper as geo_helper
import utils.visualization_helper as geo_vis


# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    api_version=(0,11,5),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

WEATHER_API_KEY = 't0Nm6euS13XNzB57Mrl49DI4rHVwU5Kt'
RANDOM_COOR_NUM=10

def get_weather_request(in_coor):
    #the coordination from Tomorrow.io is in  [longitude,latitude] format
    lon = in_coor[0]
    lat = in_coor[1]
    request_fields = 'temperature,humidity,windSpeed,precipitationIntensity'
    frequency = 'current'
     #to get real-time data for a specific coordination 
    formatted_reqeust =  f"https://api.tomorrow.io/v4/timelines?location={lat},{lon}&fields={request_fields}&timesteps={frequency}&apikey={WEATHER_API_KEY}"
    #to get real-time data for a  location
    #formatted_reqeust=f"https://api.tomorrow.io/v4/weather/realtime?location=toronto&apikey={WEATHER_API_KEY}"

    
    return formatted_reqeust

# Function to fetch data from API and send to Kafka
def fetch_and_send(in_request,eachPoint):
    print("Fetching data:")
    response = requests.get(in_request)
    
    if response.status_code == 200:
        #hourly_data = []
        print("Flushing data:")
        data = response.json()  # Assuming JSON response
 
        data= data["data"]
        latitude = eachPoint[1]
        longitude = eachPoint[0]

        curr_weather_data = data["timelines"][0]["intervals"][0]
        data_point={
            "time": curr_weather_data["startTime"],
            "lat": latitude,
            "lon": longitude,
            **curr_weather_data["values"]  # Merge all values into the dictionary
        }
        producer.send('testing_data', value=data_point)
        producer.flush()  # Flush after each send to ensure delivery
        print(f"Sent: {data_point}")


def main():
    #read coordination from forest boundary file
    forest_file_name = 'Forest_Geo/BC_Examples.json' 
    forest_name = 'Maternity Island' #use a bigger area to test
    geometry = geo_helper.get_forest_geometry_by_name(forest_file_name, forest_name)
    full_coordinations = geometry['coordinates'][0] #the output will be a list of coordinations in [longitude,latitude] format
    
    #get random points within the area
    random_points = geo_helper.get_rand_points_within_boundary(full_coordinations, num_points=RANDOM_COOR_NUM)
    for eachPoint in random_points:
        print("Processing point: {0}".format(eachPoint))
        format_request = get_weather_request(eachPoint)
        fetch_and_send(format_request,eachPoint)
    

if __name__ == "__main__":
    # Need to modify code to eriodically call the function
    main()
