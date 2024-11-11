## Prerequisites

Have your personal IAM account

## Test your account by running following testing examples

### Test the Lamda function that send forest data to Kinesis
![alt text](image.png)

Go to function fetch_forest_weather_data_to_firehose, read the basic code logic, go to the Test section, run the following testing event. Click on Test, you will send a record to Kinesis

![alt text](image-1.png)

For a success case, you will see:

![alt text](image-3.png)

And you can find timestamp in log:

![alt text](image-4.png)

### Test the Lamda function that process response from  Kinesis

Go to Lambda-> Functions -> process_forest_weather_data, run the following test event

![alt text](image-11.png)

## Verify your record was accetped in S3

For a successfully sent and processed data, you will find in S3 weather_data folder. After sending the data in lamda function, please wait few seconds before you check the S3 page 

![alt text](image-5.png)

![alt text](image-6.png)

### Debugging 
If you don't see your data, check if there is an error. GO to Firehose, find following stream:

![alt text](image-2.png)

Go to Destination error log, find the latest one (or the one that matches your send time), please notice you are seeing your local time zone (EST) here.

![alt text](image-7.png)

For more detail about the error, go to CloudWatch, open the log group (or check all groups). In our case, it's very likely the error happens in processor.

![alt text](image-8.png)

Find the log with Lst Event Time that is close to your event time, please note you are seeing UTC time here

![alt text](image-9.png)

And error usually start with [ERROR]

![alt text](image-10.png)

## Kenisis key configuration

The lamda function that process the response:

![image](https://github.com/user-attachments/assets/e7c7108c-e07d-47d9-89d4-602de9d6c31c)

S3 bucket name, the error file name prefix and data file prefix

![image](https://github.com/user-attachments/assets/c92f89ee-5e2d-4c2d-8d0d-8e639cf203a1)




