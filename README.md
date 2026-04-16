# 📡 Sensor to Web IoT Project

## 📌 Project Overview

This project implements a complete end-to-end IoT data pipeline using an ESP32 device and a web-based dashboard.

The system collects sensor data, sends it over WiFi, processes it through a backend API, stores it in a database, and visualizes it in a browser.

The goal is to understand how real-world systems integrate:

- Embedded devices (ESP32)
- Network communication (WiFi + HTTP)
- Backend services (FastAPI)
- Database storage (MongoDB)
- Frontend visualization (Dashboard)

---

## ⚠️ Project Adjustment

Originally, this project planned to use a DHT11 temperature and humidity sensor.

However, due to unreliable hardware behavior, the sensor was removed and replaced with simulated values.

### Changes made

- Temperature and humidity are simulated in code
- Additional sensors were used for real data collection

### Sensors used

- Light Sensor (digital)
- Obstacle Avoidance Sensor (digital)
- Potentiometer (analog)

This allowed the project to continue focusing on the main objective:

👉 building a complete IoT data pipeline

---

## 📊 Data Collection

### Simulated Data

- Temperature (°C)
- Humidity (%)

These values change gradually over time to mimic real sensor behavior.

### Real Sensor Data

- Light → 0 or 1
- Obstacle → 0 or 1
- Potentiometer → 0 ~ 4095

---

## 📡 Data Transmission

- ESP32 sends data via HTTP POST
- Data format: JSON
- Transmission interval: ~10 seconds
- Token-based authentication included

---

## 🔧 Hardware

- ESP32 Development Board
- Light Sensor Module
- Obstacle Avoidance Module
- Potentiometer

---

## 🏗️ System Architecture

ESP32 (Sensors) → HTTP POST → FastAPI → MongoDB → Web Dashboard

---

## ⚙️ Backend (FastAPI)

Responsibilities:

- Receive sensor data from ESP32
- Validate incoming data using Pydantic
- Authenticate requests using token
- Store data in MongoDB
- Provide API endpoints for data retrieval

### Endpoints

- POST /readings
- GET /readings/latest
- GET /readings/recent
- GET /dashboard

---

## 🔐 Authentication

All POST requests require a token.

Header format:

Authorization: Bearer my-secret-token

Unauthorized requests return:

401 Unauthorized

---

## 🗄️ Database (MongoDB)

Each record structure:

{
  "sensor_id": "esp32_01",
  "temperature": 25.2,
  "humidity": 60.8,
  "light": 1,
  "obstacle": 0,
  "potentiometer": 2300,
  "timestamp": "2026-04-03T12:00:00Z"
}

---

## 📊 Web Dashboard

The dashboard allows users to:

- View latest sensor values
- Visualize temperature and humidity trends
- Monitor sensor activity

Focus:

- Clean UI
- Real-time updates
- Easy data interpretation

---

## 🚀 How to Run

1. Start MongoDB (Docker)

docker run -d --name sensor-mongo -p 27017:27017 mongo:latest

2. Start FastAPI Server

uvicorn main:app --reload --host 0.0.0.0 --port 8000

3. Upload ESP32 Code

- Set WiFi credentials
- Set server IP (your computer IP)
- Upload using Arduino IDE

4. Open Dashboard

http://<YOUR_IP>:8000/dashboard

---

## 🧪 Testing

- WiFi connection verified
- API POST returns 200 OK
- Invalid token returns 401
- Data successfully stored in MongoDB
- Dashboard displays real-time data

---

## 🎯 Project Goals

### Basic Goals

- Send data from ESP32 to backend
- Store data in database
- Retrieve data correctly
- Display data on dashboard

### Stretch Goals

- Real-time updates (WebSocket)
- Multi-device support
- Dockerized backend
- Cloud deployment (AWS / Azure / GCP)
- CI/CD pipeline (GitHub Actions)

---

## 🧠 What I Learned

- ESP32 WiFi communication
- REST API design with FastAPI
- MongoDB for time-series data
- Full-stack system integration
- Debugging real hardware issues
- Adapting system design when hardware fails

---

## 💡 Summary

Even though the original temperature/humidity sensor was replaced, the project successfully achieves its core objective:

👉 building a complete IoT data pipeline from device to web

The system demonstrates how real-world IoT applications collect, transmit, store, and visualize data in an integrated architecture.
