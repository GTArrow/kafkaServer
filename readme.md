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
sudo apt update
sudo apt install default-jdk

## Run the kafka-server-start.sh script to start the Kafka server:
./kafka_2.13-3.8.1/bin/kafka-server-start.sh config/kraft/server.properties

