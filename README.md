# Sensor to Web IoT Project

## Project Overview

This project implements a complete end-to-end IoT data pipeline using an ESP32 and a web-based dashboard.

The system collects sensor data from embedded hardware, sends the data over WiFi using HTTP requests, stores the readings in MongoDB, and visualizes them on a real-time dashboard.

This architecture reflects real-world IoT systems used in smart homes, environmental monitoring, and industrial automation.

---

## Final Project Scope

The original plan was to use a DHT11 sensor for temperature and humidity.

However, due to hardware issues, the DHT11 sensor did not function reliably. Instead of stopping the project, the system was adjusted to ensure full pipeline completion.

### Final Implementation

Simulated Data:

* Temperature
* Humidity

Real Sensor Data:

* Light sensor
* Obstacle sensor
* Potentiometer

This approach preserved the main objective:
**building a fully working sensor-to-web IoT pipeline**

---

## Data Description

### Light Sensor

* 1 = dark
* 0 = light detected

### Obstacle Sensor

* 0 = obstacle detected
* 1 = clear

### Potentiometer

* Analog input range: 0–4095

---

## Hardware Used

* ESP32 Development Board
* Light Sensor Module
* Obstacle Detection Sensor
* Potentiometer
* Breadboard and jumper wires

---

## System Architecture

ESP32
→ HTTP POST (WiFi)
→ FastAPI Backend
→ MongoDB
→ Web Dashboard

---

## Backend and Database

### Backend (FastAPI)

Responsible for:

* Receiving sensor data
* Validating input using Pydantic
* Token authentication
* Storing data in MongoDB
* Serving API endpoints
* Serving dashboard UI

### Database (MongoDB)

Each document contains:

* sensor_id
* temperature
* humidity
* light
* obstacle
* potentiometer
* timestamp

MongoDB runs locally using Docker.

---

## API Endpoints

GET /
→ Health check

POST /readings
→ Submit sensor data (requires token)

GET /readings/latest
→ Retrieve latest reading

GET /readings/recent
→ Retrieve recent readings

GET /dashboard
→ Dashboard UI

---

## Token Authentication

The system uses Bearer Token authentication.

* ESP32 includes a token in the request header
* FastAPI validates the token before accepting data

Sensitive data is stored in a `.env` file instead of hardcoded values.

Example `.env`:

API_TOKEN=my-secret-token
MONGO_URI=mongodb://localhost:27017
DB_NAME=sensor_to_web_iot
COLLECTION_NAME=readings

---

## Docker Usage

MongoDB is run via Docker:

docker run -d --name sensor-mongo -p 27017:27017 mongo

Future improvements:

* Dockerize FastAPI backend
* Use Docker Compose
* Deploy to cloud (AWS, GCP, Azure)

---

## Dashboard Features

* Real-time sensor display
* Temperature trend chart
* Humidity trend chart
* Latest sensor values
* Light & obstacle status labels
* Manual refresh button
* Auto-refresh toggle
* Adjustable refresh interval
* Adjustable data limit
* Recent readings table

---

## Testing

Testing is implemented using pytest.

Test cases include:

* Root endpoint
* Unauthorized POST request
* Authorized POST request
* Latest data retrieval
* Recent data retrieval

---

## Specification Files

Included specification documents:

* system_spec.md
* api_spec.md
* data_model.md
* testing_spec.md

These define:

* System behavior
* API structure
* Data models
* Testing strategy

---

## Running the Project

### 1. Start MongoDB

docker run -d --name sensor-mongo -p 27017:27017 mongo

### 2. Create .env file

API_TOKEN=my-secret-token
MONGO_URI=mongodb://localhost:27017
DB_NAME=sensor_to_web_iot
COLLECTION_NAME=readings

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run FastAPI server

uvicorn main:app --reload --host 0.0.0.0 --port 8000

### 5. Open dashboard

http://YOUR_LOCAL_IP:8000/dashboard

### 6. Upload ESP32 code

* Set WiFi credentials
* Set server URL
* Set API token
* Upload to ESP32
* Monitor serial output

---

## Project Goals

### Basic Goals

* Sensor-to-API communication
* Data storage in database
* Dashboard visualization
* Token-based security

### Stretch Goals

* Full Docker setup
* Cloud deployment
* Multi-device support
* Real sensor integration

---

## What I Learned

* ESP32 networking and HTTP requests
* FastAPI backend development
* MongoDB data storage
* Token-based authentication
* Frontend dashboard design
* API testing with pytest
* Handling hardware failures

---

## Challenges

The DHT11 sensor did not function correctly.

Solution:

* Simulated temperature and humidity
* Continued development with working sensors

This ensured that the full system could still be completed.

---

## Final Result

The completed system includes:

* ESP32 data transmission
* FastAPI backend
* MongoDB storage
* Real-time dashboard
* Token authentication
* API testing

Even with hardware limitations, the full IoT pipeline was successfully implemented.

---
