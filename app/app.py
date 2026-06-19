from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import logging
import random
import time

# OpenTelemetry imports
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)

# ---------------- Logging ----------------

logging.basicConfig(
    filename='/logs/app.log',
    level=logging.INFO
)

# ---------------- Metrics ----------------

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total requests'
)

REQUEST_TIME = Histogram(
    'http_request_duration_seconds',
    'Request duration'
)

# ---------------- Tracing ----------------

resource = Resource.create(
    {"service.name": "flask-app"}
)

trace.set_tracer_provider(
    TracerProvider(resource=resource)
)

otlp_exporter = OTLPSpanExporter(
    endpoint="http://jaeger:4318/v1/traces"
)

span_processor = BatchSpanProcessor(otlp_exporter)

trace.get_tracer_provider().add_span_processor(span_processor)

FlaskInstrumentor().instrument_app(app)

# ---------------- Routes ----------------

@app.route("/")
@REQUEST_TIME.time()
def home():

    REQUEST_COUNT.inc()

    sleep_time = random.uniform(0.2,1)

    time.sleep(sleep_time)

    logging.info("Home page accessed")

    return "Observability Project"


@app.route('/metrics')
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)
