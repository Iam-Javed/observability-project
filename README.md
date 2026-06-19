# Complete Observability System (Metrics, Logs & Traces)

A complete observability stack built using Docker Compose that provides centralized monitoring, logging, and distributed tracing for a sample Flask application.

## Overview

This project demonstrates the three pillars of observability:

- **Metrics** using Prometheus
- **Logs** using Loki and Promtail
- **Traces** using Jaeger
- **Visualization** using Grafana

The entire stack is containerized and orchestrated with Docker Compose.

---

## Architecture

```text
                   User
                     |
                     ▼
               Flask Application
                     |
        --------------------------------
        |              |              |
        ▼              ▼              ▼
    Prometheus      Promtail        Jaeger
     (Metrics)         |           (Traces)
                       ▼
                     Loki
                    (Logs)
        --------------------------------
                     |
                     ▼
                  Grafana
```

---

## Tech Stack

| Component | Purpose |
|------------|---------|
| Flask | Sample Application |
| Prometheus | Metrics Collection |
| Grafana | Visualization |
| Loki | Log Aggregation |
| Promtail | Log Shipping |
| Jaeger | Distributed Tracing |
| Docker Compose | Container Orchestration |

---

## Project Structure

```text
observability-project/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── prometheus/
│   └── prometheus.yml
│
├── loki/
│   └── local-config.yaml
│
├── promtail/
│   └── config.yml
│
├── grafana/
│   └── dashboards/
│
├── logs/
│
└── docker-compose.yml
```

---

## Project Approach

### Phase 1 – Application Setup

- Built a sample Flask application.
- Added custom metrics and application logging.
- Containerized the application using Docker.

### Phase 2 – Metrics Monitoring

- Configured Prometheus to scrape application metrics.
- Monitored request count and response time.
- Visualized metrics using Grafana dashboards.

### Phase 3 – Centralized Logging

- Generated application logs.
- Used Promtail to collect logs.
- Sent logs to Loki.
- Explored logs through Grafana.

### Phase 4 – Distributed Tracing

- Integrated Jaeger for request tracing.
- Visualized request flow and latency.
- Correlated metrics, logs, and traces for troubleshooting.

---

## Components Flow

### Metrics Flow

```text
Flask Application
        │
        ▼
 Prometheus
        │
        ▼
    Grafana
```

### Logs Flow

```text
Flask Application
        │
        ▼
    app.log
        │
        ▼
    Promtail
        │
        ▼
      Loki
        │
        ▼
     Grafana
```

### Traces Flow

```text
Flask Application
        │
        ▼
      Jaeger
        │
        ▼
     Grafana
```

---

## Features

- Custom Prometheus metrics
- Application response time monitoring
- Centralized log aggregation
- Log exploration with Grafana
- Distributed request tracing
- Containerized deployment
- Single-pane observability dashboard
- Real-time troubleshooting capability

---

## Dashboards

### Metrics Dashboard

- Total HTTP Requests
- Request Duration
- Response Latency
- Application Health

### Logs Dashboard

- Application Logs
- Log Filtering
- Log Search

### Tracing Dashboard

- Request Timeline
- Trace Duration
- Span Details

---

## Use Cases

- Application Monitoring
- Performance Analysis
- Troubleshooting
- Root Cause Analysis
- Log Aggregation
- Request Tracing
- Observability Learning
- SRE and DevOps Projects

---

## Skills Demonstrated

- Docker
- Docker Compose
- Prometheus
- Grafana
- Loki
- Promtail
- Jaeger
- Monitoring
- Logging
- Distributed Tracing
- Observability
- SRE Concepts

---

## Future Enhancements

- OpenTelemetry Integration
- Alertmanager Configuration
- Email and Slack Alerts
- Kubernetes Deployment
- Node Exporter Integration
- Blackbox Exporter
- Multi-service Architecture
- CI/CD Pipeline Integration

---

## Learning Outcome

This project provides hands-on experience with implementing the three pillars of observability—Metrics, Logs, and Traces—and demonstrates how modern SRE and DevOps teams monitor applications, troubleshoot issues, and perform root cause analysis using a unified observability stack.
