# Microservices Observability in Kubernetes

This project demonstrates microservices observability in a Kubernetes environment. It consists of two services: a Hash service and a Length service, both deployed on Kubernetes with Jaeger for tracing and Prometheus for metrics.

## Setup Instructions

<!-- 1. **Prerequisites:**
    * Docker: Ensure Docker is installed and running.
    * Kubernetes (minikube or kind): Choose one and have it running.  Minikube instructions: `minikube start --driver=docker`. Kind instructions: `kind create cluster`.
    * Helm: Install Helm for package management. -->

### Initiate the Repository

    ```bash
    echo "# SHA256_check" >> README.md
    git init
    ga README.md
    mkdir hashing_service length_service
    git commit -m "init commit"
    git branch -M main
    git remote add origin git@github.com:$USERNAME/$REPO_NAME.git
    git push origin main
    ```
---

### Hashing_service

1. **Create the service branch from the main branch**

    ```bash
    git checkout -b hashing_service
    cd hashing_service
    touch main.py # add the FastAPI code
    echo "fastapi\nuvicorn" > requirements.txt    # to create the Requirments file
    git add .
    git commit -m "hashing_service fastAPI code"
    git push origin hashing_service
    ```

2. **Create the docker and kubernetes branch from the service branch**

    ```bash
    git checkout -b hashing_infra
    cd hashing_service
    touch Dockerfile # add the docker setup

    ## Test it using => docker build --tag "hash_service_test" .

    touch hash-dep.yaml # add the Kubernetes deployment configs

    ## Test the deployment using => kubectl apply -f hash-dep.yaml

    git add .
    git commit -m "Adding the dockerfile and the kubernetes deployment files"
    git push origin hashing_infra
    ```

---

### Length_service

1. **Create the service branch from the main branch**

    ```bash
    git checkout -b length_service
    cd length_service
    touch main.py # add the FastAPI code
    echo "fastapi\nuvicorn" > requirements.txt  # to create the Requirments file
    git add .
    git commit -m "length_service fastAPI code"
    git push origin length_service
    ```

2. **Create the docker and kubernetes branch from the service branch**

    ```bash
    git checkout -b length_infra
    cd length_service
    touch Dockerfile # add the docker setup

    ## Test it using => docker build --tag "hash_service_test" .

    touch hash-dep.yaml # add the Kubernetes deployment configs

    ## Test the deployment using => kubectl apply -f hash-dep.yaml

    git add .
    git commit -m "Adding the dockerfile and the kubernetes deployment files"
    git push origin length_infra
    ```

---

### Main Branch Protection

I like to protect the main branch to prevint accedental changes, code quality and standards, and collabotation. and we can do that by following the steps below:

Go to Repository Settings > Branches on GitHub.

Click Add branch protection rule.

Enter main as the protected branch. <!-- Or any branch you want -->

Enable:

- *Require pull request reviews before merging.*

- *Require status checks (CI/CD) before merging.*

- *Ensure branches are up to date before merging.*

- *Restrict who can push to main.**

**Click Create.**
