# Cloud Native Task Platform

Production-ready cloud-native task management platform built with **FastAPI**, **PostgreSQL**, **Redis**, **Docker**, and full **Observability + CI/CD** stack.

Designed to demonstrate scalable backend architecture, background processing, DevOps practices, and SRE fundamentals.

---

# Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Redis
- Prometheus
- Grafana
- Docker & Docker Compose
- GitHub Actions (CI)

---

# Architecture

## Services

- **API** – RESTful task management service
- **Worker** – Background task processor
- **PostgreSQL** – Persistent storage
- **Redis** – Task coordination & messaging
- **Prometheus** – Metrics collection
- **Grafana** – Metrics visualization
- **GitHub Actions** – CI pipeline

## Flow

Client → API → PostgreSQL  
       → Redis → Worker  
Prometheus → Scrapes `/metrics`  
Grafana → Visualizes metrics  

---

# Observability (SRE Ready)

## Metrics

### Technical Metrics
- `http_requests_total`
- `http_request_duration_seconds`
- `http_errors_total`

### Business Metrics
- `tasks_created_total`
- `tasks_in_progress`

## Golden Signals Dashboard

- Requests per Second (RPS)
- Error Rate
- Latency (p95)
- Task Creation Rate

Grafana dashboards are:
- Automatically provisioned
- Version controlled
- Persisted via Docker volume

---

# Alerts

Configured in Prometheus:

- High Error Rate
- High Latency (p95)
- API Down detection

---

# CI Pipeline

GitHub Actions workflow includes:

- Ruff (lint)
- Black (format validation)
- Pytest
- Minimum 80% coverage enforcement
- Docker image build validation

Pull Requests are blocked if any check fails.

---

# Project Structure

```

.
├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── worker/
│   ├── observability/
│   └── main.py
│
├── monitoring/
│   ├── prometheus.yml
│   ├── alerts.yml
│   └── grafana/
│
├── Dockerfile.api
├── Dockerfile.worker
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
└── .github/workflows/ci.yml

````

---

# Quick Start

## 1. Clone

```bash
git [clone](https://github.com/jeffev/cloud-native-task-platform.git)
cd cloud-native-task-platform
````

## 2. Run Full Stack

```bash
docker compose up --build
```

---

# Access Services

API

```
http://localhost:8000
```

Prometheus

```
http://localhost:9090
```

Grafana

```
http://localhost:3000
```

Default login:

```
admin / admin
```

---

# API Endpoints

## Tasks

* `GET /api/v1/tasks`
* `POST /api/v1/tasks`
* `GET /api/v1/tasks/{id}`
* `PUT /api/v1/tasks/{id}`
* `DELETE /api/v1/tasks/{id}`

## Health

* `GET /health`
* `GET /health/live`
* `GET /health/ready`

---

# Environment Variables

## API

* `DATABASE_URL`
* `REDIS_URL`
* `WORKER_COUNT`

## Worker

* `API_URL`
* `REDIS_URL`
* `WORKER_ID`
* `POLL_INTERVAL`

---

# Production Readiness Features

* Stateless API
* Horizontal worker scaling
* Redis coordination
* Dockerized infrastructure
* CI quality gate
* Observability stack
* Alert rules
* Dashboard as code
* Health checks
* Structured logging
* Request tracing (request_id)

---

# Scalability Design

* Horizontal API scaling
* Horizontal worker scaling
* Container-native architecture
* Metrics-driven monitoring
* Infrastructure as code mindset

---

# Testing

```bash
pytest
```

Coverage must remain ≥ 80%.

---

# Roadmap

* Alertmanager integration
* Slack notifications
* SLO 99.9% + Error Budget
* Burn rate alerts
* Distributed tracing
* Kubernetes manifests
* Canary deployments

---

# Purpose

This project demonstrates:

* Cloud-native backend architecture
* Background processing patterns
* Observability best practices
* DevOps pipeline implementation
* SRE monitoring fundamentals

---

# License

MIT
