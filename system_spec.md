# System Specification

## Overview

This project implements a complete end-to-end IoT data pipeline using an ESP32 device and a web-based dashboard.

The system collects sensor data, transmits it over WiFi, processes it through a backend API, stores it in a database, and visualizes it in a browser.

---

## Hardware Components

- ESP32 Development Board  
- Light Sensor (Digital)  
- Obstacle Avoidance Sensor  
- Potentiometer  

Originally, a DHT11 temperature and humidity sensor was planned. However, due to unreliable behavior, temperature and humidity values are simulated in software.

---

## System Architecture

ESP32 → HTTP POST → FastAPI → MongoDB → Dashboard

---

## Data Flow

1. ESP32 reads sensor inputs  
   - Light (digital)  
   - Obstacle (digital)  
   - Potentiometer (analog)  

2. Simulated values are generated  
   - Temperature  
   - Humidity  

3. ESP32 constructs a JSON payload  

4. ESP32 sends an HTTP POST request to the backend API  

5. FastAPI validates the request using token-based authentication  

6. Data is stored in MongoDB  

7. The dashboard retrieves data using API endpoints  

8. Data is displayed in real-time charts and summary cards  

---

## Design Goals

- Reliable sensor-to-server communication  
- Secure API using token authentication  
- Efficient time-series data storage  
- Clean and intuitive dashboard visualization  
- Modular system design for future extensions  
