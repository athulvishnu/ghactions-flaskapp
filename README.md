## Flask App with GitHub Actions + AKS

This project demonstrates a simple Flask application deployed to Azure Kubernetes Service (AKS) using GitHub Actions for CI/CD.


## Tech Stack

* Python (Flask)
* Docker
* GitHub Actions (CI/CD)
* Kubernetes
* Azure Kubernetes Service (AKS)
* Docker Hub (image registry)

## Architecture

1. Code is pushed to GitHub
2. GitHub Actions builds a Docker image
3. Image is pushed to Docker Hub
4. AKS pulls the image and deploys it
5. Service exposes the application

