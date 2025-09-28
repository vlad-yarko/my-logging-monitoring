from prometheus_client import (
    Counter,
    Gauge,
    Histogram
)


REQUESTS = Counter(
    "fastapi_requests_total",
    "Total number of HTTP requests",
    ["path", "app_name"]
)

RESPONSES = Counter(
    "fastapi_responses_total",
    "Total number of HTTP responses",
    ["path", "status_code", "app_name"]
)

EXCEPTIONS = Counter(
    "fastapi_exceptions_total",
    "Total number of HTTP exceptions",
    ["app_name"]
)

REQUEST_LATENCY = Histogram(
    "fastapi_requests_duration_seconds",
    "Request duration in seconds",
    ["path", "app_name"]
)

IN_PROGRESS = Gauge(
    "fastapi_requests_in_progress",
    "Requests currently in progress",
    ["path", "app_name"]
)

# GENERAL


# TOTAL_HTTP_REQUESTS_COUNT = Counter(
#     # "http_requests_total",
#     "fastapi_requests_total",
#     "Total number of HTTP requests"
# )

# ENDPOINT_HTTP_REQUESTS_COUNT = Counter(
#     "http_requests_by_endpoint",
#     "Number of HTTP requests per one endpoint",
#     ["method", "endpoint"]
# )


# TOTAL_IN_PROGRESS_HTTP_REQUESTS = Gauge(
#     "http_requests_in_progress_total",
#     "Total number of in-progress HTTP requests"
# )

# ENDPOINT_IN_PROGRESS_HTTP_REQUESTS = Gauge(
#     "http_requests_in_progress_by_endpoint",
#     "Number of in-progress HTTP requests per one endpoint",
#     ["method", "endpoint"]
# )


# TOTAL_HTTP_REQUEST_LATENCY = Histogram(
#     "http_requests_latency_total",
#     "Total HTTP requests latency in seconds"
# )

# ENDPOINT_HTTP_REQUEST_LATENCY = Histogram(
#     "http_requests_latency_by_endpoint",
#     "HTTP requests latency per endpoint in seconds",
#     ["method", "endpoint"]
# )


# TOTAL_HTTP_EXCEPTIONS_COUNT = Counter(
#     "http_exceptions_total", 
#     "Total number of HTTP exceptions"
# )

# ENDPOINT_HTTP_EXCEPTIONS_COUNT = Counter(
#     "http_exceptions_by_endpoint",
#     "Number of HTTP exceptions per one endpoint",
#     ["method", "endpoint"]
# )


# # /random ENDPOINT


# RANDOM_ENDPOINT_NUMBERS_COUNTER = Counter(
#     "random_endpoint_numbers_counter",
#     "Total number of output numbers of /random endpoint",
#     ["number", "endpoint"]
# )
