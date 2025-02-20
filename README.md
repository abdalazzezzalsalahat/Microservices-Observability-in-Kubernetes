# Microservices Observability in Kubernetes

This project demonstrates deploying two FastAPI microservices (hashing-service & length-service) on Kubernetes with a robust observability stack.  It incorporates best practices from both provided examples, using Jaeger for distributed tracing, Prometheus for metrics, and OpenTelemetry for unified observability.  It also includes a streamlined deployment process and GitHub branch management strategy.

## Overview

This project showcases a microservices architecture where:

- **hashing-service:**  Computes the SHA256 hash of a given text.
- **length-service:** Calculates the length of a given text string.

Both services are containerized and deployed on Kubernetes, integrated with a comprehensive observability stack.

## Technologies Used

- Python (FastAPI)
- Docker
- Kubernetes
- Jaeger for distributed tracing
- Prometheus for metrics
- OpenTelemetry for metrics and tracing collection
- GitHub Actions (Optional - for CI/CD)

## Application Components

### hashing-service

- Endpoint: `POST /hash`
- Input: `{"text": "your_text"}`
- Output: `{"hash": "sha256_hash_value"}`

### length-service

- Endpoint: `POST /length`
- Input: `{"text": "your_text"}`
- Output: `{"length": text_length}`

## Setup Guide

### 1. Start Kubernetes Cluster

```bash
minikube start
eval $(minikube docker-env)  # Configure Docker to use Minikube's environment
```

### 2. Build & Load Docker Images

```bash

docker build -t azeezmain/hashing-service:latest ./hashing_service
docker build -t azeezmain/length-service:latest ./length_service

docker push azeezmain/hashing-service:latest 
docker push azeezmain/length-service:latest

```

### 3. Run Everything with One Command (Automated deployment)

```Bash

chmod +x deploy.sh
./deploy.sh
(Your deploy.sh script should contain all the kubectl apply commands from steps 3, 4, and 5).
```

### OR Manual Deployment

#### 1. Deploy ConfigMaps

```Bash

kubectl apply -f hashing_service/hashing-config.yaml
kubectl apply -f length_service/length-config.yaml
kubectl apply -f observability/otel-configmap.yaml # For OpenTelemetry configuration
kubectl apply -f observability/prometheus-configmap.yaml # For Prometheus Config
```

#### 2. Deploy Microservices

```Bash

kubectl apply -f hashing_service/hashing-deployment.yaml
kubectl apply -f hashing_service/hashing-service.yaml
kubectl apply -f length_service/length-deployment.yaml
kubectl apply -f length_service/length-service.yaml
```

#### 3. Deploy Observability Stack

```Bash

kubectl apply -f observability/otel-collector.yaml
kubectl apply -f observability/otel-service.yaml
kubectl apply -f observability/jaeger-deployment.yaml
kubectl apply -f observability/jaeger-service.yaml
kubectl apply -f observability/prometheus-deployment.yaml
kubectl apply -f observability/prometheus-service.yaml
```

---

#### 4. Verify Deployment

```Bash

kubectl get pods -A
kubectl get services -A
```

#### 5. Access Monitoring Tools

```Bash

kubectl port-forward svc/jaeger-service 16686:16686 &  # Jaeger UI: <http://localhost:16686>
kubectl port-forward svc/prometheus-service 9090:9090 & # Prometheus UI: <http://localhost:9090>
```

---

![jaeger](Screenshot\ 2025-02-20\ 032803.png)

![prometheus](Screenshot 2025-02-20 034725.png)

#### 6. Test the Services

```Bash

curl -X POST http://localhost:8000/hash -H "Content-Type: application/json" -d '{"text": "Apple"}'
curl -X POST http://localhost:8001/length -H "Content-Type: application/json" -d '{"text": "Apple"}'
```

## GitHub Branch Management

This project uses a Gitflow-inspired branching strategy:

- **main**: The stable, production-ready branch.
- **stg**: The staging branch for pre-release testing.
- **cloud-infra**: For infrastructure changes.
- **hash-service & lngth-service**: Feature branches for developing individual services.
- **extras**: For other experimental features.

All feature branches are created from `stg`, and pull requests are **reviewed before merging** into stg and eventually main.

> GitHub branch protection rules are configured to enforce these practices.

## Troubleshooting & Debugging

- ### Check Logs

```Bash

kubectl logs -l app=otel-collector -f
kubectl logs -l app=hashing-service -f
kubectl logs -l app=length-service -f
```

- ### Restart Deployments

```Bash

kubectl rollout restart deployment hashing-service
kubectl rollout restart deployment length-service
```

## Conclusion

This project provides a solid foundation for building and monitoring microservices on Kubernetes.
The integrated observability stack with Jaeger, Prometheus, and OpenTelemetry allows for deep insights into the application's performance and behavior.
The defined branching strategy ensures a structured and reliable development process.
Adding CI/CD pipelines for automated builds and deployments to further enhance the project is considered.
