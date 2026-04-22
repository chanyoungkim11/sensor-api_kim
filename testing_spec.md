# Testing Specification

## 1. Overview

This document defines the testing strategy for the Sensor to Web IoT system.

The purpose of testing is to verify:

* API functionality
* Authentication logic
* Data validation
* Endpoint reliability

Testing is implemented using pytest and FastAPI TestClient.

---

## 2. Testing Tools

Frameworks and libraries:

* pytest
* fastapi.testclient (TestClient)
* httpx (dependency for TestClient)

---

## 3. Test Environment

* Backend: FastAPI (main.py)
* Database: MongoDB (local Docker instance)
* Environment variables loaded via .env

Tests are run locally using:

pytest

---

## 4. Test Cases

---

### 4.1 Test: Root Endpoint

#### Objective

Verify that the server is running.

#### Request

GET /

#### Expected Result

* Status code: 200
* Response contains message

---

### 4.2 Test: Unauthorized POST Request

#### Objective

Ensure that requests without a token are rejected.

#### Request

POST /readings (without Authorization header)

#### Expected Result

* Status code: 401 Unauthorized

---

### 4.3 Test: Authorized POST Request

#### Objective

Verify that valid data is accepted and stored.

#### Request

POST /readings with:

* Valid JSON payload
* Valid Authorization header

#### Expected Result

* Status code: 200
* Response contains "data saved"

---

### 4.4 Test: Get Latest Reading

#### Objective

Verify retrieval of the most recent sensor data.

#### Request

GET /readings/latest

#### Expected Result

* Status code: 200
* Response contains latest data or message

---

### 4.5 Test: Get Recent Readings

#### Objective

Verify retrieval of multiple recent records.

#### Request

GET /readings/recent

#### Expected Result

* Status code: 200
* Response is a list of readings

---

## 5. Sample Test Code

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

API_TOKEN = "my-secret-token"

def test_root():
response = client.get("/")
assert response.status_code == 200

def test_post_readings_unauthorized():
data = {
"sensor_id": "test_device",
"temperature": 25.0,
"humidity": 60.0,
"light": 1,
"obstacle": 0,
"potentiometer": 100
}

```
response = client.post("/readings", json=data)
assert response.status_code == 401
```

def test_post_readings_authorized():
data = {
"sensor_id": "test_device",
"temperature": 25.0,
"humidity": 60.0,
"light": 1,
"obstacle": 0,
"potentiometer": 100
}

```
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

response = client.post("/readings", json=data, headers=headers)
assert response.status_code == 200
```

def test_get_latest():
response = client.get("/readings/latest")
assert response.status_code == 200

def test_get_recent():
response = client.get("/readings/recent")
assert response.status_code == 200

---

## 6. Test Coverage

The following features are covered:

* Server availability
* Authentication logic
* Data submission
* Data retrieval
* API response validation

---

## 7. Error Handling Tests

Potential additional tests:

* Invalid JSON format
* Missing fields
* Wrong data types
* Invalid token format

---

## 8. Limitations

* Tests rely on local MongoDB instance
* No mocking of database
* No performance testing

---

## 9. Future Improvements

* Add database mocking
* Add integration tests
* Add load testing
* Automate tests with CI/CD (GitHub Actions)

---
