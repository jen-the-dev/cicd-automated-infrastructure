# CI/CD Pipeline & Automated Infrastructure
DevOps-focused portfolio sample for ANZSCO 261312 (Developer Programmer).

## Why this project helps your visa/job-hunt profile
- Shows you can ship software end-to-end, not just write application code.
- Demonstrates infrastructure automation and deployment lifecycle knowledge.
- Proves practical CI/CD competency expected in modern software teams.

## Tech stack
- Python Flask app
- Docker
- Kubernetes manifests
- Terraform (AWS starter)
- GitHub Actions

## MVP scope
- Containerized HTTP service.
- Kubernetes deployment + service manifest.
- Terraform resources for baseline cloud infrastructure.
- CI pipeline that validates app syntax, builds Docker image, and validates Terraform.

## Repository structure
- `app/` - sample Python service.
- `k8s/` - deployment manifests.
- `terraform/` - infrastructure-as-code definitions.
- `.github/workflows/ci-cd.yml` - pipeline automation.

## Quick start
1. `pip install -r app/requirements.txt`
2. `python app/main.py`
3. `docker build -t portfolio-cicd-app .`
4. `terraform -chdir=terraform init -backend=false && terraform -chdir=terraform validate`

## Next upgrades (recommended before interviews)
- Add test stage, image scanning, and environment promotion gates.
- Add Helm chart or Kustomize overlays for staging/production.
- Wire Terraform state backend and deploy workflow with OIDC.
