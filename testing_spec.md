# Testing Specification

## Objective

Ensure that the entire IoT pipeline works correctly from sensor input to dashboard visualization.

---

## Test Cases

### 1. WiFi Connection

- ESP32 connects successfully
- IP address is assigned

Expected result:
Device prints a valid IP address in the serial monitor.

---

### 2. API Communication

- ESP32 sends an HTTP POST request to the backend

Expected result:
HTTP response code is 200.

---

### 3. Authentication

- Valid token → success
- Invalid token → failure

Expected result:
Invalid or missing token returns 401 Unauthorized.

---

### 4. Database Storage

- Data is stored in MongoDB

Expected result:
A new document appears in the `readings` collection after a valid POST request.

---

### 5. Data Retrieval

Test endpoints:

- `/readings/latest`
- `/readings/recent`

Expected result:
Returned data matches values previously sent by the ESP32.

---

### 6. Dashboard

- Latest sensor values are displayed correctly
- Temperature and humidity charts render correctly
- Dashboard updates when new data is stored

Expected result:
The dashboard reflects real-time or recent sensor data accurately.

---

## Expected Outcome

- All components communicate correctly
- Data is stored and retrieved accurately
- The dashboard displays sensor information clearly
- Token protection prevents unauthorized data submission
