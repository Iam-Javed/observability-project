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

<img width="1099" height="522" alt="image" src="https://github.com/user-attachments/assets/4e3bad87-7f83-4e0d-927e-7081f6099dc4" />

<img width="876" height="261" alt="image" src="https://github.com/user-attachments/assets/0f51dce3-51c2-4a80-9807-2ec72572343d" />

<img width="1355" height="419" alt="image" src="https://github.com/user-attachments/assets/8ea01eff-81cd-4349-8839-b64016e3cbfb" />

<img width="486" height="114" alt="image" src="https://github.com/user-attachments/assets/45e5f3dd-f699-4a1a-b578-973277193535" />

<img width="1366" height="371" alt="image" src="https://github.com/user-attachments/assets/78f54f58-cb4d-44bd-9d9d-b924b7a5f9ef" />

<img width="1366" height="371" alt="image" src="https://github.com/user-attachments/assets/03021610-1f3c-44f9-9d56-6d790f5e8163" />

<img width="1352" height="633" alt="image" src="https://github.com/user-attachments/assets/482b60ad-8284-4895-a348-c575ea72cef5" />

<img width="1348" height="623" alt="image" src="https://github.com/user-attachments/assets/e874cd22-6f4c-480c-bac0-946fbec3aabc" />

<img width="1344" height="645" alt="image" src="https://github.com/user-attachments/assets/953ab75e-3f24-4437-966c-f4a42cc5ef00" />

<img width="1343" height="644" alt="image" src="https://github.com/user-attachments/assets/d5d6699a-ec85-478b-bdc7-dbd150c3aec5" />
