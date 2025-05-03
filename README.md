# Building SaaS Applications on Amazon EKS using GitOps

> A complete multi-language (Python + Golang) SaaS automation blueprint powered by Amazon EKS, GitOps with FluxCD, Helm, and optionally ArgoCD.

---

## Workshop Overview

This repository implements the [AWS Workshop Studio](https://catalog.workshops.aws/) on **Building SaaS applications on Amazon EKS using GitOps**, including full automation for:

- Tenant onboarding/offboarding
- Multi-tier SaaS tenant strategy
- Kubernetes namespace and HelmRelease templating
- FluxCD GitOps delivery
- Optional ArgoCD integration
- Python and Golang-based automation

---

## 📂 Folder Structure

```
AWS-GitOps-EKS/
├── automation/
│   ├── python/
│   │   ├── onboard.py
│   │   └── offboard.py
│   └── go/
│       ├── main.go
│       └── utils.go
├── tenants/
│   ├── tenant-template.yaml
│   ├── namespace-template.yaml
│   └── tiers/
│       ├── basic-values.yaml
│       ├── standard-values.yaml
│       └── premium-values.yaml
├── flux/
│   ├── tenants/
│   │   ├── tenant-*.yaml
│   │   └── namespace-*.yaml
│   └── kustomization.yaml
├── .github/
│   └── workflows/
│       └── flux-deploy.yaml
├── cleanup/
│   └── cleanup.sh
└── README.md
```

---

## Prerequisites

- AWS Account (EKS access)
- `eksctl`, `kubectl`, `flux`, `helm`, `python3`, and `go` installed
- GitHub repository created: `https://github.com/AryanSharma9917/AWS-GitOps-EKS`

---

## Quick Start

### 1. Create EKS Cluster

```bash
eksctl create cluster --name saas-eks-cluster --region us-west-2 --nodes 3
```

---

### 2. Bootstrap Flux on the Cluster

```bash
flux bootstrap github \
  --owner=AryanSharma9917 \
  --repository=AWS-GitOps-EKS \
  --branch=main \
  --path=./flux \
  --personal
```

---

### 3. Onboard a Tenant

#### Using Python

```bash
cd automation/python
python3 onboard.py --name tenant1 --tier premium
```

#### Using Go

```bash
cd automation/go
go run main.go tenant1 premium
```

---

### 4. Offboard a Tenant

```bash
cd automation/python
python3 offboard.py --name tenant1
```

---

## SaaS Tier Strategies

Each tenant is deployed with tier-specific configurations:

| Tier     | CPU    | Memory | Features             |
|----------|--------|--------|----------------------|
| Basic    | 250m   | 256Mi  | Limited              |
| Standard | 500m   | 512Mi  | Moderate             |
| Premium  | 1000m  | 1Gi    | High performance     |

Defined in `tenants/tiers/*.yaml`.

---

## GitOps with Flux

All onboarding/offboarding operations are committed to Git under the `flux/tenants/` folder and picked up by **Flux** via:

```yaml
# flux/kustomization.yaml
resources:
  - ./tenants/namespace-tenant1.yaml
  - ./tenants/tenant-tenant1.yaml
```

---

## GitHub Actions Integration

Automated via `.github/workflows/flux-deploy.yaml`. It:

- Installs Flux CLI
- Adds changes to `flux/` or `tenants/` directory
- Commits and pushes updates to GitHub

This triggers Flux to sync the latest tenant states.

---

## ArgoCD Integration (Optional)

To deploy via ArgoCD:

```bash
kubectl apply -f argo-app.yaml
```

#### Example `argo-app.yaml`

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: saas-gitops
  namespace: argocd
spec:
  source:
    repoURL: 'https://github.com/AryanSharma9917/AWS-GitOps-EKS'
    path: flux
    targetRevision: HEAD
  destination:
    server: 'https://kubernetes.default.svc'
    namespace: flux-system
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

---

##  Cleanup Resources

```bash
bash cleanup/cleanup.sh
```

---

## Features

- [x] Multi-tier SaaS onboarding
- [x] Namespace + HelmRelease templating
- [x] Flux GitOps delivery
- [x] Python + Go automation
- [x] GitHub Actions CI
- [ ] ArgoCD support (optional)
- [x] Easy cleanup

---

<!-- ## 📸 Screenshots

> (You can add screenshots of Flux UI, ArgoCD UI, HelmRelease YAMLs, EKS cluster dashboard, etc.) -->

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- AWS SaaS Factory Workshop
- [FluxCD](https://fluxcd.io)
- [ArgoCD](https://argoproj.github.io)
- [Helm](https://helm.sh)
