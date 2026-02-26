# 🚀 Notification Prioritization Engine

An intelligent notification decision system built using **FastAPI** that classifies incoming notification events into:

* ✅ **Now** – Send immediately
* ⏳ **Later** – Queue for delayed delivery
* ❌ **Never** – Suppress permanently

This system reduces alert fatigue, prevents duplicate notifications, supports configurable business rules, and logs a clear explanation for every decision.

---

# 📌 Problem Statement

Modern applications generate excessive notifications. Without prioritization:

* Users experience alert fatigue
* Duplicate alerts reduce trust
* Important notifications get ignored
* No transparency in why notifications are sent

This engine solves these challenges using layered decision logic, rule overrides, deduplication, fatigue handling, and audit logging.

---

# 🏗️ Architecture Overview

```
Incoming Event
      ↓
Layer 1 – Expiration Check
      ↓
Layer 2 – Hard Rules (Security / Muted Users)
      ↓
Layer 3 – Deduplication Engine
      ↓
Layer 4 – Fatigue Engine
      ↓
Layer 5 – Configurable Rule Engine
      ↓
Final Decision (Now / Later / Never)
      ↓
Audit Logging
```

---

# 🧠 Core Features

## ✅ 1. Notification Classification

Each event is classified into:

* **Now** – High priority, send immediately
* **Later** – Queue for scheduled delivery
* **Never** – Suppressed due to rules or duplication

---

## ✅ 2. Deduplication Engine

Prevents:

* Exact duplicate notifications
* Near-duplicate alerts
* Rapid repeated events

File:

```
app/dedupe_engine.py
```

---

## ✅ 3. Alert Fatigue Reduction

Reduces user overload by:

* Checking recent notification frequency
* Detecting burst patterns
* Delaying non-critical alerts

File:

```
app/fatigue_engine.py
```

---

## ✅ 4. Hard Rule Overrides

Examples:

* Security alerts → **Always Now**
* Muted users → **Always Never**
* Expired notifications → **Never**

File:

```
app/decision_engine.py
```

---

## ✅ 5. Human-Configurable Rules

Rules can be modified without redeploying the system.

File:

```
app/rule_engine.py
```

---

## ✅ 6. Clear Decision Logging

Every event stores:

* Decision (Now/Later/Never)
* Exact reason for decision
* Timestamp

File:

```
app/audit_logger.py
```

---

## ✅ 7. Fail-Safe Design

If any dependent component fails:

* System defaults to safe behavior
* Does not crash
* Logs fallback reason

---

# 📂 Project Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requirements.txt
├── migrations/
│   └── schema.sql
└── app/
    ├── main.py
    ├── decision_engine.py
    ├── rule_engine.py
    ├── dedupe_engine.py
    ├── fatigue_engine.py
    ├── scheduler.py
    ├── audit_logger.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    ├── config.py
    └── utils.py
```

---

# ⚙️ Tech Stack

* Python 3.10+
* FastAPI
* Uvicorn
* SQL Database
* Docker & Docker Compose
* OpenAPI (Swagger Documentation)

---

# 🚀 Running the Project

## 🔹 Option 1: Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run server:

```
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🔹 Option 2: Run with Docker

Build and start:

```
docker-compose up --build
```

Open:

```
http://localhost:8000/docs
```

---

# 📡 API Endpoints

## 🔹 POST `/events`

Creates and evaluates a notification event.

### Request Body

```json
{
  "user_id": "123",
  "event_type": "security",
  "message": "New login detected",
  "expires_at": "2026-02-26T20:14:12.432Z"
}
```

### Response

```json
{
  "id": 1,
  "decision": "Now",
  "reason": "Security override rule"
}
```

---

## 🔹 GET `/`

Health check endpoint.

Response:

```json
{
  "status": "healthy"
}
```

---

# 🧪 Decision Logic Layers

### Layer 1 – Expiration Check

If expired → **Never**

### Layer 2 – Hard Rules

* Security event → **Now**
* Muted user → **Never**

### Layer 3 – Deduplication

If duplicate → **Never**

### Layer 4 – Fatigue Control

If user overloaded → **Later**

### Layer 5 – Configurable Rules

Custom business logic applied

---

# 🔍 Example Scenarios

| Scenario                 | Decision | Reason                     |
| ------------------------ | -------- | -------------------------- |
| Security login alert     | Now      | Security override rule     |
| Repeated same alert      | Never    | Duplicate detected         |
| Too many alerts recently | Later    | Fatigue threshold exceeded |
| Expired event            | Never    | Expired                    |

---

# 🛡️ Safety & Reliability

* Graceful failure handling
* Audit trail for transparency
* Configurable without redeploy
* Clean modular architecture

---

# 📈 Future Improvements

* AI-based scoring engine
* Notification analytics dashboard
* User-level dynamic thresholds
* Redis caching for performance
* Async event processing

---

# 🎥 Demo Walkthrough

1. Start server
2. Open `/docs`
3. Send test event
4. Show classification
5. Explain layered decision logic
6. Show audit reasoning

---

# 👩‍💻 Author

**A Lahari **
Notification Prioritization Engine
Built for intelligent alert management systems.

---

