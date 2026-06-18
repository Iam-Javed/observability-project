from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import logging
import random
import time

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total requests'
)

REQUEST_TIME = Histogram(
    'http_request_duration_seconds',
    'Request duration'
)


@app.route("/")
def home():

    start = time.time()

    logging.info("Home endpoint accessed")

    delay = random.uniform(0.2,2)

    time.sleep(delay)

    REQUEST_COUNT.inc()

    REQUEST_TIME.observe(time.time()-start)

    return "Application running"


@app.route("/error")
def error():

    logging.error("Error endpoint hit")

    return "Internal Error",500


@app.route("/metrics")
def metrics():

    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
