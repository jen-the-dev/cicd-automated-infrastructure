# CI/CD Pipeline & Automated Infrastructure
Delivery-and-operations portfolio project aligned to ANZSCO 261312 (Developer Programmer).

## Recruiter quick view
- Focus: software delivery lifecycle, automation, and infrastructure-as-code.
- Business scenario: containerized service promoted through repeatable validation and deployment artifacts.
- Stack signal: Python/Flask, Docker, Kubernetes manifests, Terraform, GitHub Actions.
- Current maturity: strong platform engineering scaffold showing practical deployment literacy.

## ANZSCO 261312 competency mapping
- **Developing and packaging application software**
  - Implemented service endpoint and container runtime packaging.
  - Defined runnable local workflow from source to container image.
- **Designing and maintaining deployment processes**
  - Built CI pipeline stages for code validation, image build, and Terraform validation.
  - Added consistent repository structure separating app, runtime manifests, and IaC.
- **Implementing infrastructure and environment automation**
  - Authored Terraform baseline resources (ECR/ECS starter footprint).
  - Added Kubernetes deployment and service manifests for orchestrated runtime.
- **Supporting reliability and maintainability**
  - Included health endpoint and readiness probe configuration.
  - Established documented extension path for promotion gates and secure cloud auth.

## Evidence map (where reviewers should look)
- Application service: `app/main.py`
- Container build: `Dockerfile`
- Kubernetes runtime: `k8s/deployment.yaml`
- Infrastructure as code: `terraform/main.tf`
- CI/CD automation: `.github/workflows/ci-cd.yml`

## Tech stack
- Python Flask app
- Docker
- Kubernetes
- Terraform (AWS starter)
- GitHub Actions

## Implemented scope (current)
- Health-reporting web service.
- Container image definition for deployment.
- Kubernetes deployment + service with readiness probe.
- Terraform resource definitions for baseline cloud infrastructure.
- CI pipeline with Python compile check, Docker build, and Terraform validate.

## Quick start
1. `pip install -r app/requirements.txt`
2. `python app/main.py`
3. `docker build -t portfolio-cicd-app .`
4. `terraform -chdir=terraform init -backend=false && terraform -chdir=terraform validate`

## 5-minute demo flow for interviews
1. Show local app health endpoint.
2. Build container and explain runtime contract.
3. Walk through Kubernetes deployment/service/readiness probe setup.
4. Explain Terraform resources and how they support deployment.
5. Show CI workflow sequence and discuss promotion-hardening next steps.

## Next milestones to strengthen application evidence
- Add automated test stage, image scanning, and staged release gates.
- Add Helm/Kustomize overlays for environment-specific deployments.
- Configure Terraform remote state and OIDC-based deployment credentials.
