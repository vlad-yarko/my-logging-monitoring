import logging
import random
import time

from fastapi import FastAPI, HTTPException, Request
from starlette.responses import Response

from prometheus_client import (
    generate_latest,
    CONTENT_TYPE_LATEST
)

from metrics import (
    REQUESTS,
    RESPONSES,
    EXCEPTIONS,
    REQUEST_LATENCY,
    IN_PROGRESS
)

# from metrics import (
#     TOTAL_HTTP_REQUESTS_COUNT,
#     ENDPOINT_HTTP_REQUESTS_COUNT,
#     TOTAL_IN_PROGRESS_HTTP_REQUESTS,
#     ENDPOINT_IN_PROGRESS_HTTP_REQUESTS,
#     TOTAL_HTTP_REQUEST_LATENCY,
#     ENDPOINT_HTTP_REQUEST_LATENCY,
#     TOTAL_HTTP_EXCEPTIONS_COUNT,
#     ENDPOINT_HTTP_EXCEPTIONS_COUNT,
#     RANDOM_ENDPOINT_NUMBERS_COUNTER
# )


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


app = FastAPI()

APP_NAME = "fastapi-backend"


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    path = request.url.path
    method = request.method
    
    REQUESTS.labels(
        path=path,
        app_name=APP_NAME,
        # method=method
    ).inc()

    IN_PROGRESS.labels(
        path=path,
        app_name=APP_NAME,
        # method=method
    ).inc()
    start_time = time.time()

    try:
        response = await call_next(request)
        status_code = str(response.status_code)

        RESPONSES.labels(
            path=path,
            status_code=status_code,
            app_name=APP_NAME,
            # method=method
        ).inc()
        
        if status_code != str(200):
            EXCEPTIONS.labels(
                # path=path,
                app_name=APP_NAME,
                # method=method
            ).inc()
            
        return response

    except Exception as e:
        EXCEPTIONS.labels(
            path=path,
            app_name=APP_NAME,
            # method=method
        ).inc()
        raise e

    finally:
        time_elapsed = time.time() - start_time
        REQUEST_LATENCY.labels(
            path=path,
            app_name=APP_NAME,
            # method=method
        ).observe(time_elapsed)
        
        IN_PROGRESS.labels(
            path=path,
            app_name=APP_NAME,
            # method=method
        ).dec()



@app.get("/metrics")
async def metrics():
    response = Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
    return response


@app.get("/")
async def root():
    return {"message": "ROOT"}


@app.get("/status/{status_code}")
async def status_hand(status_code: int):
    if status_code != 200:
        raise HTTPException(
            detail=f"Error {status_code}",
            status_code=status_code
        )
    return {"message": "OK"}


@app.get("/random")
async def random_hand(request: Request):
    number = random.randint(1, 5)
    # RANDOM_ENDPOINT_NUMBERS_COUNTER.labels(
    #     number=str(number),
    #     method=request.method,
    #     endpoint=request.url.path
    # )
    return {"number": number}


# @app.middleware("http")
# async def metrics_middleware(request: Request, call_next):
#     # For histogram (latency)
#     start_time = time.time()
    
#     # Gauge IN PROGRESS
#     TOTAL_IN_PROGRESS_HTTP_REQUESTS.inc()
#     ENDPOINT_IN_PROGRESS_HTTP_REQUESTS.labels(
#         method=request.method,
#         endpoint=request.url.path
#     ).inc()
    
#     try:
#         response = await call_next(request)
        
#         # HTTP requests counter
#         TOTAL_HTTP_REQUESTS_COUNT.inc()
#         ENDPOINT_HTTP_REQUESTS_COUNT.labels(
#             method=request.method,
#             endpoint=request.url.path
#         ).inc()
        
#         # For histogram (latency)
#         elapsed = time.time() - start_time
#         TOTAL_HTTP_REQUEST_LATENCY.observe(elapsed)
#         ENDPOINT_HTTP_REQUEST_LATENCY.labels(
#             method=request.method,
#             endpoint=request.url.path
#         )
        
#         return response
    
#     except Exception as e:
        
#         TOTAL_HTTP_EXCEPTIONS_COUNT.inc()
#         ENDPOINT_HTTP_EXCEPTIONS_COUNT.labels(
#             method=request.method,
#             endpoint=request.url.path
#         ).inc()
#         raise e
    
#     finally:
        
#         # Gauge IN PROGRESS
#         TOTAL_IN_PROGRESS_HTTP_REQUESTS.dec()
#         ENDPOINT_IN_PROGRESS_HTTP_REQUESTS.labels(
#             method=request.method,
#             endpoint=request.url.path
#         ).dec()
