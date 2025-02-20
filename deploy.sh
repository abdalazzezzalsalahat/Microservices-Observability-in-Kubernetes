#!/bin/bash

set -e
set -o pipefail
set -u

NAMESPACE="observe"

if ! kubectl cluster-info >/dev/null 2>&1; then
    echo "Kubernetes cluster is not running!"
    exit 1
fi

kubectl create namespace $NAMESPACE

echo " Starting deployment..."

echo "Applying ConfigMaps..."
kubectl apply -n $NAMESPACE -f observability/hashing-config.yaml
kubectl apply -n $NAMESPACE -f observability/length-config.yaml
kubectl apply -n $NAMESPACE -f observability/otel-configmap.yaml
kubectl apply -n $NAMESPACE -f observability/prometheus-configmap.yaml


echo "Deploying Hash and Length Services..."
kubectl apply -n $NAMESPACE -f hashing_service/hashing-deployment.yaml
kubectl apply -n $NAMESPACE -f length_service/length-deployment.yaml

echo " Deploying OpenTelemetry Collector..."
kubectl apply -n $NAMESPACE -f observability/otel-collector.yaml

echo "Deploying Jaeger..."
kubectl apply -n $NAMESPACE -f observability/jaeger-deployment.yaml

echo "Deploying Prometheus..."
kubectl apply -n $NAMESPACE -f observability/prometheus-deployment.yaml

echo "Checking deployment status..."
kubectl get pods -A
kubectl get services -A

echo "Deployment completed successfully!"

echo "Run curl -X POST http://localhost:8000/hash -H "Content-Type: application/json" -d '{"text": "apple"}' to hash a string"
echo "____________________________________________________________________"
echo "Run curl -X POST http://localhost:8001/length -H "Content-Type: application/json" -d '{"text": "apple"}' to check the string length"
echo "____________________________________________________________________"
echo "Access Jaeger: http://localhost:16686"
echo "Access Prometheus: http://localhost:9090"
