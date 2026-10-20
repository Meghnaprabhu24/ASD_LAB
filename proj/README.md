# ASD_LAB – End-to-End DevOps Pipeline (Experiment 10)

A Flask task-manager app with a full CI/CD pipeline: Git/GitHub -> GitHub Actions (lint, test) -> Docker build -> Docker Hub -> deploy.

## Run locally
    pip install -r requirements.txt
    pytest
    python app.py            # http://localhost:5000

## Run with Docker
    docker build -t asd-devops-app .
    docker run -d -p 5000:5000 asd-devops-app

or `docker compose up -d --build`

## Pipeline
No secrets needed: the image is pushed to GitHub Container Registry (ghcr.io) using the built-in `GITHUB_TOKEN`.
View it under the repo's **Packages** section after the first successful run on `main`.
