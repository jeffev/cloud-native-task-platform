# Cloud Native Task Platform

A cloud-native task management platform built with FastAPI, Docker, and Docker Compose. This platform provides a scalable solution for managing and processing tasks in a distributed environment.

## Architecture

The platform consists of the following components:

- **API Service**: FastAPI-based REST API for task management
- **Worker Service**: Background task processing service
- **PostgreSQL**: Primary database for task storage
- **Redis**: Caching and message queuing
- **Docker Compose**: Container orchestration

## Features

- ✅ RESTful API for task CRUD operations
- ✅ Background task processing
- ✅ Containerized deployment
- ✅ Health checks and monitoring
- ✅ Scalable worker architecture
- ✅ Database persistence
- ✅ Docker Compose orchestration

## Project Structure

```
.
├── api/
│   ├── main.py          # FastAPI application entry point
│   ├── routes.py        # API endpoints
│   ├── database.py      # Database configuration
│   └── models.py        # Pydantic and SQLAlchemy models
├── worker/
│   └── worker.py        # Background task processor
├── requirements.txt     # Python dependencies
├── Dockerfile.api       # API service Dockerfile
├── Dockerfile.worker    # Worker service Dockerfile
├── docker-compose.yml   # Container orchestration
└── README.md           # This file
```

## Quick Start

### Prerequisites

- Docker
- Docker Compose
- Python 3.11+ (for local development)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd cloud-native-task-platform
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API locally**
   ```bash
   cd api
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Run the worker locally**
   ```bash
   cd worker
   python worker.py
   ```

### Docker Deployment

1. **Build and start all services**
   ```bash
   docker-compose up -d
   ```

2. **View logs**
   ```bash
   docker-compose logs -f
   ```

3. **Stop services**
   ```bash
   docker-compose down
   ```

## API Endpoints

### Task Management

- `GET /api/v1/tasks` - Get all tasks
- `GET /api/v1/tasks/{task_id}` - Get specific task
- `POST /api/v1/tasks` - Create new task
- `PUT /api/v1/tasks/{task_id}` - Update task
- `DELETE /api/v1/tasks/{task_id}` - Delete task
- `POST /api/v1/tasks/{task_id}/execute` - Execute task

### Health Check

- `GET /health` - API health check
- `GET /` - Root endpoint

## Environment Variables

### API Service

- `DATABASE_URL` - Database connection string
- `REDIS_URL` - Redis connection string
- `WORKER_COUNT` - Number of worker instances

### Worker Service

- `API_URL` - API service URL
- `WORKER_ID` - Unique worker identifier
- `POLL_INTERVAL` - Task polling interval in seconds
- `REDIS_URL` - Redis connection string

## Configuration

### Database

The platform uses PostgreSQL as the primary database. Default configuration:

- Database: `task_platform`
- User: `task_user`
- Password: `task_password`
- Port: `5432`

### Redis

Redis is used for caching and message queuing. Default configuration:

- Port: `6379`

## Development

### Adding New Features

1. Update the API models in `api/models.py`
2. Add new endpoints in `api/routes.py`
3. Update the worker logic in `worker/worker.py` if needed
4. Update `requirements.txt` for new dependencies
5. Test locally before containerizing

### Testing

```bash
# Run API tests
cd api
pytest

# Run worker tests
cd worker
pytest
```

## Monitoring

### Health Checks

Each service includes health checks:

- **API**: HTTP endpoint `/health`
- **Database**: PostgreSQL connection check
- **Redis**: Redis ping command
- **Worker**: Python import check

### Logs

Monitor service logs with:

```bash
docker-compose logs -f [service-name]
```

## Production Deployment

For production deployment:

1. Update environment variables with production values
2. Configure proper secrets management
3. Set up monitoring and alerting
4. Configure load balancing
5. Set up backup strategies

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions:

- Create an issue in the repository
- Check the documentation
- Review the code examples