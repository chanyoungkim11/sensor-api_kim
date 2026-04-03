📡 Sensor to Web IoT Project
📌 Project Overview

This project is about building a simple end-to-end IoT system that collects sensor data using an ESP32 and displays it on a web dashboard.

The main goal is to understand how different parts of a real-world system connect together, including:

Embedded device (ESP32)
Network communication (WiFi + HTTP)
Backend server (FastAPI)
Database (MongoDB)
Frontend visualization
⚠️ Project Adjustment

Originally, this project was planned to use a DHT sensor (DHT11/DHT22) to measure temperature and humidity.

However, during implementation, the DHT11 sensor did not work reliably, so I decided to change the approach instead of spending too much time debugging hardware issues.

✔️ Changes made
Temperature and humidity values are now simulated in code
Added other sensors to collect actual input data

This allowed me to continue focusing on the main goal of the project:
👉 building the data pipeline and system integration

📊 Data Collection

The system now uses a mix of simulated and real sensor data.

🔹 Simulated Data
Temperature (°C)
Humidity (%)

These values are generated in a way that changes slowly over time so they behave similarly to real sensor readings.

🔹 Real Sensor Data

The following sensors are used:

Light Sensor (Digital)
→ detects light / dark (0 or 1)
Obstacle Avoidance Sensor
→ detects nearby objects (0 or 1)
Potentiometer
→ provides continuous analog values (0 ~ 4095)
📡 Data Transmission
Data is sent from ESP32 every ~60 seconds
Communication uses WiFi + HTTP POST
Data format is JSON
🔧 Hardware
ESP32 Dev Board
Light sensor module
Obstacle avoidance module
Potentiometer
🏗️ System Architecture
ESP32 (Sensors)
    ↓
FastAPI Backend
    ↓
MongoDB
    ↓
Web Dashboard
⚙️ Backend (FastAPI)

The backend is responsible for:

Receiving sensor data from ESP32
Validating incoming data
Storing data in MongoDB
Providing API endpoints for data retrieval

Additional improvement planned:

Simple token-based authentication
🗄️ Database (MongoDB)

Each record is structured as:

{
  "sensor_id": "esp32_01",
  "temperature": 25.2,
  "humidity": 60.8,
  "light": 1,
  "obstacle": 0,
  "potentiometer": 2300,
  "timestamp": "2026-04-03T12:00:00Z"
}
📊 Web Dashboard

The dashboard will:

Show latest sensor values
Display historical data using charts
Allow basic data exploration

Focus:

Clean UI
Easy-to-read data
🎯 Project Goals
✅ Basic Goals
Send data from ESP32 to backend
Store data in database
Retrieve data correctly
Visualize data on web dashboard
🚀 Stretch Goals
Real-time updates (polling or WebSocket)
Support multiple devices
Docker-based deployment
Cloud deployment (AWS / Azure / GCP)
CI/CD with GitHub Actions
🧠 What I Learned
How ESP32 communicates over WiFi
How to design a simple REST API
How to handle time-series data
How different parts of a system connect together
How to adapt when hardware doesn’t work as expected
💡 Note

Even though I couldn’t use the actual temperature/humidity sensor, the project still achieves its main goal:

👉 building a working IoT data pipeline from device to web.

🎯 Summary

👉 The sensors changed, but the core objective remained the same:
building a complete IoT data pipeline.
