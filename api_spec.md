# API Specification

## 1. Overview

This document defines the REST API used in the Sensor to Web IoT system.

The API allows:

* Sensor devices (ESP32) to send data
* Clients (dashboard) to retrieve stored data

All data is transferred in JSON format over HTTP.

---

## 2. Base URL

http://localhost:8000

(Replace with deployed server URL if hosted remotely)

---

## 3. Authentication

The API uses Bearer Token authentication for protected endpoints.

### Header Format

Authorization: Bearer <API_TOKEN>

---

## 4. Endpoints

---

### 4.1 GET /

#### Description

Health check endpoint to verify that the server is running.

#### Request

GET /

#### Response

Status: 200 OK

{
"message": "Server is running"
}

---

### 4.2 POST /readings

#### Description

Submit sensor data to the backend.

#### Authentication

Required

#### Headers

Authorization: Bearer <API_TOKEN>
Content-Type: application/json

#### Request Body

{
"sensor_id": "string",
"temperature": float,
"humidity": float,
"light": int,
"obstacle": int,
"potentiometer": int
}

#### Example

{
"sensor_id": "esp32_01",
"temperature": 25.4,
"humidity": 60.2,
"light": 0,
"obstacle": 1,
"potentiometer": 1200
}

#### Response

Status: 200 OK

{
"message": "data saved",
"inserted_id": "string"
}

#### Error Responses

401 Unauthorized
→ Missing or invalid token

422 Unprocessable Entity
→ Invalid data format

---

### 4.3 GET /readings/latest

#### Description

Retrieve the most recent sensor reading.

#### Request

GET /readings/latest

#### Response

Status: 200 OK

{
"sensor_id": "esp32_01",
"temperature": 25.4,
"humidity": 60.2,
"light": 0,
"obstacle": 1,
"potentiometer": 1200,
"timestamp": "ISO datetime"
}

#### Notes

* Returns latest entry based on timestamp
* Returns message if no data exists

---

### 4.4 GET /readings/recent

#### Description

Retrieve a list of recent sensor readings.

#### Query Parameters

limit (optional, default = 20)

#### Request

GET /readings/recent?limit=20

#### Response

Status: 200 OK

[
{
"sensor_id": "esp32_01",
"temperature": 25.4,
"humidity": 60.2,
"light": 0,
"obstacle": 1,
"potentiometer": 1200,
"timestamp": "ISO datetime"
},
...
]

#### Notes

* Data is returned in chronological order
* Limit controls number of records returned

---

### 4.5 GET /dashboard

#### Description

Serves the web dashboard interface.

#### Request

GET /dashboard

#### Response

Status: 200 OK
HTML content

---

## 5. Data Validation

All incoming POST data is validated using Pydantic.

Validation rules:

* sensor_id must be string
* temperature must be float
* humidity must be float
* light must be integer
* obstacle must be integer
* potentiometer must be integer

Invalid data results in HTTP 422 error.

---

## 6. Status Codes Summary

200 OK
→ Successful request

401 Unauthorized
→ Invalid or missing token

422 Unprocessable Entity
→ Validation error

500 Internal Server Error
→ Server/database error

---

## 7. Security Considerations

* Token-based authentication required for POST requests
* Sensitive values stored in environment variables
* No public write access to database

---

## 8. Future Improvements

* HTTPS support
* OAuth or JWT authentication
* Rate limiting
* Device-specific authentication tokens
* API versioning (v1, v2)

---
