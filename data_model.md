# Data Model Specification

## Collection Name

readings

---

## Document Schema

```json
{
  "sensor_id": "string",
  "temperature": "float",
  "humidity": "float",
  "light": "int",
  "obstacle": "int",
  "potentiometer": "int",
  "timestamp": "datetime"
}

Field Descriptions
sensor_id
Unique identifier of the ESP32 device
temperature
Simulated temperature in degrees Celsius
humidity
Simulated humidity percentage
light
Digital light detection (0 or 1)
obstacle
Obstacle detection (0 or 1)
potentiometer
Analog value (0–4095)
timestamp
UTC timestamp when the reading is stored
Example Document
{
  "sensor_id": "esp32_01",
  "temperature": 24.4,
  "humidity": 59.9,
  "light": 1,
  "obstacle": 1,
  "potentiometer": 871,
  "timestamp": "2026-04-15T20:59:20"
}
Indexing Strategy

Recommended index:

timestamp

Used for efficient sorting and time-based queries.
