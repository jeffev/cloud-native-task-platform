from prometheus_client import Counter, Gauge, Histogram

# -----------------------------------
# HTTP Metrics
# -----------------------------------

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status_code"],
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"],
)

ERROR_COUNT = Counter(
    "http_errors_total",
    "Total HTTP 5xx errors",
    ["method", "endpoint"],
)

# -----------------------------------
# Business Metrics
# -----------------------------------

TASKS_CREATED_TOTAL = Counter(
    "tasks_created_total",
    "Total number of tasks created",
)

TASKS_IN_PROGRESS = Gauge(
    "tasks_in_progress",
    "Current number of tasks in progress",
)
