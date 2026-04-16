# API Specification

## Authentication

All POST requests require token authentication.

### Header

Authorization: Bearer my-secret-token

---

## POST /readings

### Description

Receives sensor data from the ESP32 and stores it in MongoDB.

---

### Headers

Authorization: Bearer <token>  
Content-Type: application/json  

---

### Request Body

```json
{
  "sensor_id": "esp32_01",
  "temperature": 25.0,
  "humidity": 60.0,
  "light": 1,
  "obstacle": 0,
  "potentiometer": 1200
}

Success Response
{
  "message": "data saved",
  "inserted_id": "string"
}
Error Response
{
  "detail": "Unauthorized"
}
Status Codes
200 OK → success
401 Unauthorized → invalid token
GET /readings/latest
Description

Returns the most recent sensor reading.

Response Example
{
  "_id": "string",
  "sensor_id": "esp32_01",
  "temperature": 24.5,
  "humidity": 59.8,
  "light": 1,
  "obstacle": 1,
  "potentiometer": 800,
  "timestamp": "2026-04-15T21:00:00"
}
GET /readings/recent
Description

Returns the most recent N sensor readings.

Query Parameters
limit (optional, default = 20)
Example Request

GET /readings/recent?limit=20

Response Example
[
  {
    "sensor_id": "esp32_01",
    "temperature": 24.3,
    "humidity": 60.2,
    "light": 1,
    "obstacle": 0,
    "potentiometer": 500,
    "timestamp": "2026-04-15T20:50:00"
  }
]
