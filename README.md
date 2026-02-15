# Cloud Native Task Platform

A cloud-native task management platform built with **FastAPI**, **PostgreSQL**, **Redis**, and **Docker**.
Designed to demonstrate scalable architecture patterns, background processing, and containerized deployment.

---

## Tech Stack

* Python 3.11
* FastAPI
* SQLAlchemy
* Pydantic
* PostgreSQL
* Redis
* Docker
* Docker Compose

---

## Architecture Overview

The platform is composed of:

* **API Service** – RESTful interface for task management
* **Worker Service** – Background task processor
* **PostgreSQL** – Persistent task storage
* **Redis** – Caching and task coordination
* **Docker Compose** – Multi-container orchestration

### Flow

Client → API → PostgreSQL
       → Redis → Worker

---

## Key Features

* RESTful API for task CRUD operations
* Background task execution
* Stateless API design
* Scalable worker architecture
* Containerized services
* Health check endpoints
* Database persistence
* Service isolation

---

## Project Structure

```
.
├── api/
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   └── models.py
├── worker/
│   └── worker.py
├── requirements.txt
├── Dockerfile.api
├── Dockerfile.worker
├── docker-compose.yml
└── README.md
```

---

## Quick Start

### Prerequisites

* Docker
* Docker Compose
* Python 3.11+ (for local development)

---

## Running Locally (Development Mode)

### 1. Clone repository

```bash
git clone <repository-url>
cd cloud-native-task-platform
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run API

```bash
cd api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Run Worker

```bash
cd worker
python worker.py
```

---

## Running with Docker (Recommended)

### Start services

```bash
docker-compose up -d
```

### View logs

```bash
docker-compose logs -f
```

### Stop services

```bash
docker-compose down
```

---

## API Endpoints

### Task Management

* `GET /api/v1/tasks`
* `GET /api/v1/tasks/{task_id}`
* `POST /api/v1/tasks`
* `PUT /api/v1/tasks/{task_id}`
* `DELETE /api/v1/tasks/{task_id}`
* `POST /api/v1/tasks/{task_id}/execute`

### Health Check

* `GET /health`
* `GET /`

---

## Environment Variables

### API Service

* `DATABASE_URL`
* `REDIS_URL`
* `WORKER_COUNT`

### Worker Service

* `API_URL`
* `WORKER_ID`
* `POLL_INTERVAL`
* `REDIS_URL`

---

## Default Configuration

### PostgreSQL

* Database: `task_platform`
* User: `task_user`
* Password: `task_password`
* Port: `5432`

### Redis

* Port: `6379`

---

## Scalability Design

* Stateless API
* Horizontal worker scaling
* Redis-based coordination
* Container-ready services
* Service isolation
* Infrastructure portability

---

## Monitoring & Health Checks

Each service exposes health validation:

* API → `/health`
* PostgreSQL → connection check
* Redis → ping validation
* Worker → process heartbeat

Logs:

```bash
docker-compose logs -f [service-name]
```

---

## Production Considerations

For production environments:

* Use managed PostgreSQL (e.g., RDS)
* Use managed Redis (e.g., ElastiCache)
* Deploy containers to Kubernetes
* Configure CI/CD pipeline
* Enable centralized logging
* Implement observability (Prometheus + Grafana)
* Configure secret management
* Add autoscaling policies

---

## Testing

```bash
cd api
pytest

cd worker
pytest
```

---

## Purpose

This project was created to demonstrate:

* Cloud-native design principles
* Background task processing patterns
* Containerized microservice architecture
* Distributed system fundamentals
* Scalability-oriented backend design

---

## Roadmap (Next Improvements)

* Add authentication (JWT)
* Add OpenAPI documentation customization
* Add CI pipeline (GitHub Actions)
* Add integration tests
* Add metrics endpoint
* Add Kubernetes deployment manifests

---

## License

MIT License