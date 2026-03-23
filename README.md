# Sensor to Web IoT Project

## Project Overview

This project aims to design and implement a complete end-to-end Internet of Things (IoT) data pipeline that collects environmental sensor readings and presents them through a web-based dashboard.

The goal of this project is to gain practical experience building a real-world system that integrates embedded hardware, network communication, backend API services, database storage, and frontend data visualization.

This type of architecture is commonly used in smart homes, environmental monitoring systems, industrial automation, and data logging platforms.

---

## Data Collection

The system will collect environmental data including:

- Temperature (°C)
- Humidity (%)

These measurements are useful for:

- Indoor climate monitoring
- Smart building automation
- Environmental trend analysis
- Predictive control systems such as HVAC optimization

Sensor readings will be transmitted every **60 seconds** over WiFi using HTTP requests.

---

## Hardware Plan

The project will use the following hardware components:

- **ESP32 Microcontroller**
  - WiFi-enabled embedded development board
  - Responsible for collecting sensor readings and transmitting data to the backend API

- **DHT22 Temperature and Humidity Sensor**
  - Digital sensor capable of measuring environmental temperature and humidity
  - Suitable for indoor environmental monitoring applications

The ESP32 will periodically read sensor values and send structured JSON data packets to the backend server.

---

## System Architecture

The system will follow a typical IoT data pipeline structure:
Sensor Device (ESP32 + DHT22)
        ↓
REST API (FastAPI)
        ↓
MongoDB Database
        ↓
Web Dashboard


This architecture reflects real production IoT deployments where edge devices communicate with cloud services for data storage and visualization.

---

## Backend Design

A RESTful backend service will be implemented using **FastAPI**.

The backend will:

- Accept sensor readings via HTTP POST requests
- Validate incoming data using Pydantic schemas
- Store time-series readings in a MongoDB database
- Provide endpoints for retrieving historical data
- Compute statistical summaries such as minimum, maximum, and average values

To improve system security, token-based authentication may be implemented to prevent unauthorized devices from submitting data.

---

## Database Design

MongoDB will be used to store sensor readings due to its flexibility and suitability for time-series data.

Each record will contain:

- Sensor ID
- Temperature
- Humidity
- Timestamp (UTC)
- Optional location metadata

Indexes will be configured to support efficient queries for recent readings and time-range filtering.

An optional data retention policy may automatically delete records older than 30 days.

---

## Web Dashboard

A lightweight web dashboard will allow users to:

- View the most recent sensor readings
- Explore historical data trends through charts
- Analyze environmental statistics over configurable time ranges
- Monitor data from multiple sensors (future enhancement)

The focus of the dashboard will be usability and clear data presentation.

---

## Project Goals

### Basic Goals

- Sensor device successfully transmits data to the backend API over WiFi
- Backend validates and stores incoming readings
- Database queries return correct historical results
- Dashboard visualizes recent and past sensor data

### Stretch Goals

- Real-time data updates using polling or WebSockets
- Support for multiple sensor devices
- Deployment of backend services using Docker containers
- Cloud hosting on platforms such as AWS, Azure, or GCP
- Continuous integration and deployment using GitHub Actions
- Secure token-based data submission

---

## Expected Learning Outcomes

Through this project I aim to develop practical skills in:

- Embedded device networking and IoT communication
- REST API design and implementation
- Time-series database management
- Cloud deployment workflows
- Full-stack system integration
- Real-world software architecture design
