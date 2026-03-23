# sensor-api_kim

# Sensor to Web IoT Project

## Project Overview
This project will build a full data pipeline that collects environmental sensor data and displays it on a web dashboard.

## Hardware
I plan to use an ESP32 microcontroller with a DHT22 temperature and humidity sensor.

The sensor will measure:
- Temperature (°C)
- Humidity (%)

Data will be sent every 60 seconds over WiFi.

## Backend
A REST API will be built using FastAPI.

The API will:
- Receive sensor readings
- Validate input data
- Store readings in MongoDB
- Provide endpoints for querying historical data and statistics

## Database
MongoDB will be used to store time-series sensor readings.

## Dashboard
A simple web dashboard will display:
- Latest reading
- Historical charts
- Min / Max / Average statistics

## Goals
Basic goals:
- Sensor sends data to API
- Data stored in database
- Dashboard shows charts

Stretch goals:
- Real-time updates
- Multiple sensors
- Cloud deployment using Docker
