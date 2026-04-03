📡 Sensor to Web IoT Project
Project Overview

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

What I changed:
Temperature and humidity values are now simulated in code
Added other sensors to collect actual input data

This allowed me to continue working on the main goal of the project, which is the data pipeline and system integration, rather than focusing only on one sensor.

📊 Data Collection

The system now uses a mix of simulated and real sensor data.

Simulated Data
Temperature (°C)
Humidity (%)

These values are generated in a way that changes slowly over time so they behave similar to real sensor readings.

Real Sensor Data

I used the following sensors:

Light Sensor (Digital)
→ detects light / dark (0 or 1)
Obstacle Avoidance Sensor
→ detects nearby objects (0 or 1)
Potentiometer
→ provides continuous analog values (0 ~ 4095)
📡 Data Transmission
ESP32 sends data every ~60 seconds
Uses WiFi + HTTP POST
Data is formatted as JSON
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

The backend handles:

Receiving data from ESP32
Validating input
Storing data in MongoDB
Providing API endpoints for data retrieval

I also plan to add simple authentication later.

🗄️ Database (MongoDB)

Each record looks like this:

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
Display graphs over time
Allow simple data exploration

The main focus is making the data easy to understand.

🎯 Goals
Basic
Send data from ESP32 → backend
Store data in database
Retrieve and display data on web
Stretch
Real-time updates
Multiple devices
Docker deployment
Cloud hosting
CI/CD
🧠 What I Learned
How ESP32 communicates over WiFi
How to design a simple REST API
How to store and query time-series data
How different parts of a system connect together
How to adjust a project when hardware doesn't work as expected
💡 Note

Even though I couldn’t use the actual temperature/humidity sensor, the project still achieves its main goal:

→ building a working IoT data pipeline from device to web.
