# System Specification

## 1. System Overview

This system is an end-to-end IoT data pipeline that collects sensor data from an ESP32 device, transmits the data over WiFi to a backend API, stores the data in a database, and displays the information on a web dashboard.

The system is designed to simulate a real-world IoT architecture used in applications such as environmental monitoring, smart home systems, and industrial sensing.

---

## 2. System Components

### 2.1 Hardware Layer

Device:

* ESP32 microcontroller

Sensors:

* Light sensor (digital)
* Obstacle sensor (digital)
* Potentiometer (analog)

Simulated Sensors:

* Temperature
* Humidity

Responsibilities:

* Read sensor values
* Generate simulated values
* Send data via HTTP POST request

---

### 2.2 Network Layer

Protocol:

* HTTP (REST API)

Communication:

* ESP32 sends JSON payloads to backend

Security:

* Bearer Token Authentication

---

### 2.3 Backend Layer

Framework:

* FastAPI

Responsibilities:

* Validate incoming data using Pydantic
* Authenticate requests using API token
* Store data in MongoDB
* Provide API endpoints for data retrieval
* Serve dashboard frontend

---

### 2.4 Database Layer

Database:

* MongoDB

Structure:

* Collection: readings

Each document includes:

* sensor_id (string)
* temperature (float)
* humidity (float)
* light (int)
* obstacle (int)
* potentiometer (int)
* timestamp (datetime)

---

### 2.5 Frontend Layer

Technology:

* HTML + CSS + JavaScript
* Chart.js

Features:

* Display latest sensor values
* Render temperature and humidity charts
* Show recent readings table
* Auto-refresh and manual refresh controls

---

## 3. Data Flow

### Step-by-step pipeline:

1. ESP32 reads sensor values
2. ESP32 generates JSON payload
3. ESP32 sends HTTP POST request to backend
4. Backend validates token
5. Backend validates data format
6. Backend stores data in MongoDB
7. Frontend requests data via GET endpoints
8. Backend returns data
9. Dashboard updates UI

---

## 4. Data Format

### Example JSON Payload

{
"sensor_id": "esp32_01",
"temperature": 25.3,
"humidity": 60.5,
"light": 0,
"obstacle": 1,
"potentiometer": 1200
}

---

## 5. Sensor Logic

### Light Sensor

* 1 = dark
* 0 = light detected

### Obstacle Sensor

* 0 = obstacle detected
* 1 = clear

---

## 6. Authentication

The system uses a Bearer Token for securing data submission.

Process:

1. ESP32 sends request with Authorization header
2. Backend compares token with stored value
3. If valid → accept request
4. If invalid → return 401 Unauthorized

---

## 7. Error Handling

Backend handles the following cases:

* Missing token → 401 Unauthorized
* Invalid token → 401 Unauthorized
* Invalid data format → 422 Validation Error
* Database failure → 500 Internal Server Error

ESP32 handles:

* WiFi reconnection attempts
* HTTP request failure logging

---

## 8. Performance Considerations

* Data is sent every ~1 second
* MongoDB handles time-series data efficiently
* Dashboard fetch interval is configurable
* Charts limit number of displayed records

---

## 9. Deployment Strategy

Current:

* Backend runs locally
* MongoDB runs in Docker

Future:

* Dockerize backend
* Use Docker Compose
* Deploy to cloud (AWS / GCP / Azure)

---

## 10. Scalability Considerations

Potential improvements:

* Support multiple sensor devices
* Use message queues (Kafka / MQTT)
* Switch to time-series database (InfluxDB)
* Add authentication per device
* Implement rate limiting

---

## 11. Security Considerations

* Token-based authentication
* Environment variables for secrets
* No hardcoded credentials in backend
* Restricted API access

---

## 12. Limitations

* Temperature and humidity are simulated
* No HTTPS (local environment)
* Single device support
* Basic authentication only

---

## 13. Future Improvements

* Real sensor integration (DHT22)
* Cloud deployment
* HTTPS support
* User authentication system
* Historical analytics
* Alerts / notifications

---
