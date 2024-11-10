# Setting up and Running Kafka on Windows with WSL2

This guide helps you set up and run Apache Kafka on Windows using WSL2. It follows instructions provided in the Confluent blog post: [Set Up and Run Kafka on Windows/Linux WSL 2](https://www.confluent.io/blog/set-up-and-run-kafka-on-windows-linux-wsl-2/).

## Prerequisites

- **Windows 10 or Windows 11** with **WSL2** installed
- **Ubuntu** or another Linux distribution installed on WSL2
- **Java** (Kafka requires Java to run)

## Steps to Set Up Kafka

### 1. Install Java

In your WSL2 terminal, install Java:

```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt install openjdk-17-jdk -y
```

### 2. Got to Kafka folder then run the kafka-server-start.sh script to start the Kafka server:
```bash
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
bin/kafka-server-start.sh config/kraft/server.properties
```
## Environment setup issue

If you are seeing kafka module issue for example
```bash
ModuleNotFoundError: No module named 'kafka.vendor.six.moves'
```
Try to install kafka python from git directly
```bash
pip install --break-system-packages git+https://github.com/dpkp/kafka-python.git
```