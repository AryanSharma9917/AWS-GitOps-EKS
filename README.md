# AWS-GitOps-EKS


'''
You said:
Workshop Studio


Building SaaS applications on Amazon EKS using GitOps

Introduction

Setup

Lab 1: App & Infra Blueprint

Lab 2: SaaS Tier Strategy

Lab 3: Automating Tenant Onboarding/Offboarding

Lab 4: Deployment Automation with Flux

[Optional] Lab 5: Multi-tenant Staggered Deployments
Summary
Cleanup
Building SaaS applications on Amazon EKS using GitOps
Building SaaS applications on Amazon EKS using GitOps
Building SaaS applications on Amazon EKS using GitOps
The Kubernetes infrastructure automation tool chain provides Software-as-a-Service (SaaS) builders with a rich collection of constructs that can be used to support the complex onboarding and provisioning requirements of SaaS environments.

In this session, you will look at a fully working SaaS on EKS DevOps automation solution that addresses the unique nuances that teams must support in multi-tenant environments. The goal is to create an end-to-end solution that uses Flux v2 , Argo Workflows , Helm , and other Kubernetes  tools to provision and configure tenant Amazon Elastic Kubernetes Service (EKS)  environments, supporting a range of tiers and deployment models.

The solution aims to provide a platform experience that can simplify DevOps processes in SaaS multi-tenant environments.

High Level

Duration
Here is the corrected table with each lab title correctly linked and dependencies properly mapped:

Lab Title	Time Required	Dependency
Introduction	10 mins	None
Lab 1: App & Infra Blueprint	20 mins	Introduction
Lab 2: SaaS Tier Strategy	25 mins	Lab 1: App & Infra Blueprint
Lab 3: Automating Tenant Provisioning	25 mins	Lab 2: SaaS Tier Strategy
Lab 4: Deployment Automation with Flux	30 mins	Lab 3: Automating Tenant Provisioning
Lab 5: Multi-tenant Staggered Deployments	30 mins	Lab 4: Deployment Automation with Flux
Please note that as of today, this workshop is meant to be used during AWS-run events, if running this workshop in your own account the artefacts created in the course of this workshop will likely exceed the AWS free tier. You are responsible for the cost of the AWS services while running this workshop's deployment. There is no additional cost for using the workshop aside from the cost of the resources it creates.

Next
© 2008 - 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved.
Privacy policy
Terms of use
Cookie preferences 


with language is gonna be used over here and can i upload it on gthub?


ChatGPT said:
The workshop content you've shared is built around Amazon EKS (Elastic Kubernetes Service) and GitOps practices. Here’s a breakdown of what languages and tools are typically involved in such a workshop, and your second question answered too:

🔧 Technologies and Languages Likely Used
Infrastructure as Code (IaC):

YAML — for Kubernetes manifests, Helm charts, and Flux configurations.

Helm — for Kubernetes templating.

Flux v2 — GitOps tool for Kubernetes.

Argo Workflows — typically defined in YAML.

Scripting/Automation:

Bash/Shell scripts — to automate setup, provisioning, and teardown.

Possibly Python or Go scripts — if there’s any custom tooling (optional).

Cloud Platform:

AWS CLI / eksctl — for interacting with EKS and other AWS services.

GitOps Tools:

Flux v2 (GitOps controller using YAML for automation).

Helm (templating tool used within GitOps).

Kustomize (optional, for managing Kubernetes configs).

📁 Can You Upload This Workshop to GitHub?
Yes — you can upload your version of this workshop to GitHub, but keep these points in mind:

✅ Allowed:
If you are creating your own version of the workshop or modifying it for personal/team learning.

If AWS has provided this workshop as part of a public GitHub repository or a publicly available tutorial (many of AWS's workshops are open source).

❌ Not Allowed (without permission):
Reuploading copyrighted or proprietary content from AWS if it's not publicly licensed.

Branding it as your own if you're not modifying it significantly or giving attribution.

💡 Tip: If you're unsure, check if the content is already available on AWS Workshops GitHub or their official workshop portal.

Would you like help structuring the GitHub repo (e.g., folders for each lab, README template)?







You said:
okay so Ill be doing this both in python and golang so now give me each and everythig that I need to do from scratch and I want complete detals with complete code with file name and folders and everyrhing if you cant give whole in one chat then at last dropa message Ill type more for the rest of the part


ChatGPT said:
Updated saved memory
Great — since you're implementing the “Building SaaS applications on Amazon EKS using GitOps” workshop in both Python and Go, I’ll give you a full, production-level scaffold that aligns with the labs in the workshop. We’ll build this out in phases, covering:

✅ Project structure (directories, files)

✅ Initial setup (IAM roles, EKS cluster, Git repo structure)

✅ Lab-wise implementation in Python and Go, clearly separated

✅ Automation using GitOps (Flux v2, Helm, Argo Workflows)

✅ Cleanup and summary

🔧 Step 1: Folder & File Structure (Python + Go version)
pgsql
Copy
Edit
saas-on-eks-gitops/
├── README.md
├── infra/
│   ├── cluster.yaml
│   ├── eksctl-create.sh
│   └── flux/
│       └── flux-install.yaml
├── tenants/
│   └── tenant-template.yaml
├── helm/
│   └── app-chart/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           └── deployment.yaml
├── automation/
│   ├── go/
│   │   ├── main.go
│   │   └── onboard.go
│   └── python/
│       ├── main.py
│       └── onboard.py
├── argo/
│   └── workflows/
│       └── tenant-onboarding.yaml
├── flux/
│   └── kustomization.yaml
└── cleanup/
    └── cleanup.sh
✅ Step 2: EKS + Flux Setup
infra/cluster.yaml — EKS cluster definition (used by eksctl)
yaml
Copy
Edit
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: saas-eks-cluster
  region: us-west-2

nodeGroups:
  - name: ng-1
    instanceType: t3.medium
    desiredCapacity: 2
infra/eksctl-create.sh — Create the EKS cluster
bash
Copy
Edit
#!/bin/bash
eksctl create cluster -f cluster.yaml
Make executable: chmod +x infra/eksctl-create.sh
Run: ./infra/eksctl-create.sh

✅ Step 3: Install Flux
infra/flux/flux-install.yaml
yaml
Copy
Edit
# Install Flux v2 (we assume you're using the GitHub bootstrap model)
flux bootstrap github \
  --owner=<your-github-username> \
  --repository=saas-on-eks-gitops \
  --branch=main \
  --path=flux \
  --personal
You’ll need Flux CLI installed

✅ Step 4: Helm Chart for App
helm/app-chart/Chart.yaml
yaml
Copy
Edit
apiVersion: v2
name: app-chart
description: A sample SaaS tenant app
version: 0.1.0
helm/app-chart/templates/deployment.yaml
yaml
Copy
Edit
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Values.tenantName }}-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ .Values.tenantName }}-app
  template:
    metadata:
      labels:
        app: {{ .Values.tenantName }}-app
    spec:
      containers:
        - name: app
          image: {{ .Values.image }}
          ports:
            - containerPort: 80
helm/app-chart/values.yaml
yaml
Copy
Edit
tenantName: tenant1
image: nginx:latest
✅ Step 5: Tenant Template
tenants/tenant-template.yaml
yaml
Copy
Edit
apiVersion: helm.toolkit.fluxcd.io/v2beta1
kind: HelmRelease
metadata:
  name: tenant-{{ .tenantName }}
  namespace: tenants
spec:
  interval: 1m
  releaseName: {{ .tenantName }}-app
  chart:
    spec:
      chart: ./helm/app-chart
      sourceRef:
        kind: GitRepository
        name: saas-repo
        namespace: flux-system
  values:
    tenantName: {{ .tenantName }}
    image: {{ .image }}
This can be processed with Python or Go (next step).

✅ Step 6: Automation Scripts
automation/python/onboard.py — Python onboarding script
python
Copy
Edit
import os
import yaml

TEMPLATE_PATH = "tenants/tenant-template.yaml"
OUTPUT_PATH = "flux/tenants/tenant-{name}.yaml"

def onboard_tenant(name, image="nginx:latest"):
    with open(TEMPLATE_PATH, 'r') as f:
        content = f.read()
    
    processed = content.replace("{{ .tenantName }}", name).replace("{{ .image }}", image)

    with open(OUTPUT_PATH.format(name=name), 'w') as f:
        f.write(processed)
    
    print(f"Tenant {name} config created at {OUTPUT_PATH.format(name=name)}")

if __name__ == "__main__":
    onboard_tenant("tenant1")
automation/go/onboard.go — Go onboarding script
go
Copy
Edit
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	template, err := os.ReadFile("tenants/tenant-template.yaml")
	if err != nil {
		panic(err)
	}

	tenantName := "tenant1"
	image := "nginx:latest"

	output := strings.ReplaceAll(string(template), "{{ .tenantName }}", tenantName)
	output = strings.ReplaceAll(output, "{{ .image }}", image)

	outPath := fmt.Sprintf("flux/tenants/tenant-%s.yaml", tenantName)
	os.WriteFile(outPath, []byte(output), 0644)

	fmt.Printf("Tenant config written to %s\n", outPath)
}
✅ Step 7: Argo Workflow Example
argo/workflows/tenant-onboarding.yaml
yaml
Copy
Edit
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: onboard-tenant
spec:
  entrypoint: onboard
  templates:
    - name: onboard
      container:
        image: python:3.9
        command: [python]
        args: ["/scripts/onboard.py"]
        volumeMounts:
          - name: scripts
            mountPath: /scripts
      volumes:
        - name: scripts
          configMap:
            name: tenant-onboard-script
✅ Step 8: Cleanup Script
cleanup/cleanup.sh
bash
Copy
Edit
#!/bin/bash

eksctl delete cluster --name saas-eks-cluster
If this structure looks good, I’ll continue with detailed code for:

Each lab with Helm and GitOps automation.

Handling tiers (Lab 2)

Automating onboarding/offboarding

Staggered deployment patterns

Multi-tenant Flux setups

👉 Type "continue" to proceed with the remaining lab implementations in code.







You said:
continue


ChatGPT said:
Perfect — let’s continue by implementing the remaining labs with Python, Golang, and GitOps patterns in line with the workshop. We're now diving into:

🔬 Lab 2: SaaS Tier Strategy
This lab focuses on defining multiple tiers of tenants — e.g., Basic, Standard, and Premium — with differing resource allocations and feature sets.

✅ Folder Update:
pgsql
Copy
Edit
tenants/
├── tenant-template.yaml
├── tiers/
│   ├── basic-values.yaml
│   ├── standard-values.yaml
│   └── premium-values.yaml
🧾 tenants/tiers/basic-values.yaml
yaml
Copy
Edit
tenantName: {{ .tenantName }}
image: nginx:stable
resources:
  limits:
    cpu: "250m"
    memory: "256Mi"
🧾 tenants/tiers/standard-values.yaml
yaml
Copy
Edit
tenantName: {{ .tenantName }}
image: nginx:latest
resources:
  limits:
    cpu: "500m"
    memory: "512Mi"
🧾 tenants/tiers/premium-values.yaml
yaml
Copy
Edit
tenantName: {{ .tenantName }}
image: nginx:latest
resources:
  limits:
    cpu: "1000m"
    memory: "1Gi"
🔄 Python: automation/python/onboard.py (Updated for tiers)
python
Copy
Edit
def onboard_tenant(name, tier="standard"):
    with open(TEMPLATE_PATH, 'r') as f:
        template = f.read()
    
    tier_file = f"tenants/tiers/{tier}-values.yaml"
    with open(tier_file, 'r') as f:
        tier_values = f.read()

    processed = template.replace("{{ .tenantName }}", name).replace("{{ .image }}", "nginx:latest")
    processed += "\n" + tier_values

    with open(OUTPUT_PATH.format(name=name), 'w') as f:
        f.write(processed)

    print(f"Tenant '{name}' with tier '{tier}' created.")
🔄 Go: automation/go/onboard.go (Updated for tiers)
go
Copy
Edit
tierPath := fmt.Sprintf("tenants/tiers/%s-values.yaml", tier)
tierData, err := os.ReadFile(tierPath)
if err != nil {
    panic(err)
}

output += "\n" + string(tierData)
🤖 Lab 3: Automating Tenant Onboarding/Offboarding
This includes creating tenant namespace, HelmRelease, and removing them on offboarding.

✅ Flux GitOps Directory Structure:
markdown
Copy
Edit
flux/
└── tenants/
    ├── tenant-tenant1.yaml
    ├── tenant-tenant2.yaml
    └── ...
🧾 Namespace Template: tenants/namespace-template.yaml
yaml
Copy
Edit
apiVersion: v1
kind: Namespace
metadata:
  name: {{ .tenantName }}
🧾 Update Python onboard.py to write namespace file
python
Copy
Edit
namespace_template = "tenants/namespace-template.yaml"
with open(namespace_template, 'r') as f:
    ns = f.read().replace("{{ .tenantName }}", name)

with open(f"flux/tenants/namespace-{name}.yaml", 'w') as f:
    f.write(ns)
❌ Offboarding Script automation/python/offboard.py
python
Copy
Edit
import os

def offboard_tenant(name):
    helm_file = f"flux/tenants/tenant-{name}.yaml"
    ns_file = f"flux/tenants/namespace-{name}.yaml"
    for file in [helm_file, ns_file]:
        if os.path.exists(file):
            os.remove(file)
            print(f"Removed {file}")

offboard_tenant("tenant1")
🚀 Lab 4: Deployment Automation with Flux
Flux uses Kustomize to deploy all tenants via GitOps.

🧾 flux/kustomization.yaml
yaml
Copy
Edit
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - ./tenants/namespace-tenant1.yaml
  - ./tenants/tenant-tenant1.yaml
  - ./tenants/namespace-tenant2.yaml
  - ./tenants/tenant-tenant2.yaml
Add to Flux: flux-system/kustomization.yaml
yaml
Copy
Edit
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: tenants-kustomization
  namespace: flux-system
spec:
  interval: 1m
  path: ./flux
  prune: true
  sourceRef:
    kind: GitRepository
    name: saas-repo
🧠 [Optional] Lab 5: Multi-tenant Staggered Deployments
Deploy tenants in batches or with staggered rollouts (premium first, then standard).

🧾 flux/kustomization-premium.yaml
yaml
Copy
Edit
spec:
  dependsOn:
    - name: base-kustomization
  path: ./flux/premium
And separate folders:

Copy
Edit
flux/
├── premium/
│   ├── tenant-tenant1.yaml
├── standard/
│   └── tenant-tenant2.yaml
🧹 Final Cleanup (cleanup/cleanup.sh)
bash
Copy
Edit
#!/bin/bash
eksctl delete cluster --name saas-eks-cluster
rm -rf flux/tenants/*
✅ At This Point You Have:
Full SaaS GitOps infra in Python and Go

Multi-tier onboarding logic

Flux-driven Helm deployments

Tenant management (create/delete)

Optional staged rollout

Would you like me to now:

Help you set up GitHub Actions or ArgoCD to auto-deploy?

Convert this into a working public GitHub repo scaffold?

Just let me know how you'd like to proceed!







You said:
yes please


ChatGPT said:
Updated saved memory
Great — let’s now set up GitHub Actions to automate your SaaS app deployment using Flux with multi-language support (Python & Go).

⚙️ GitHub Actions for GitOps with Flux
📁 Folder Structure Update:
markdown
Copy
Edit
.github/
└── workflows/
    └── flux-deploy.yaml
🧾 .github/workflows/flux-deploy.yaml
yaml
Copy
Edit
name: Flux GitOps Deployment

on:
  push:
    branches: [ main ]
    paths:
      - 'flux/**'
      - 'tenants/**'
      - '.github/workflows/flux-deploy.yaml'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Setup Flux CLI
      uses: fluxcd/flux2/action@main
      with:
        install-flux: true

    - name: Commit & Push Flux changes
      run: |
        git config user.name github-actions
        git config user.email github-actions@github.com
        git add flux/ tenants/
        git commit -m "Automated Flux update" || echo "No changes to commit"
        git push
This ensures that whenever you make changes to:

Flux Kustomizations

HelmRelease templates

Tenant onboarding files
The GitHub Action will commit and push them, triggering Flux in your EKS cluster.

🚀 ArgoCD Integration (Optional Alternative to GitHub Actions)
Deploy ArgoCD on your EKS cluster:

bash
Copy
Edit
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
Port forward UI (locally):

bash
Copy
Edit
kubectl port-forward svc/argocd-server -n argocd 8080:443
Login (default user = admin):

bash
Copy
Edit
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo
Create ArgoCD App:

yaml
Copy
Edit
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: saas-gitops
  namespace: argocd
spec:
  destination:
    name: ''
    namespace: flux-system
    server: 'https://kubernetes.default.svc'
  source:
    path: flux
    repoURL: 'https://github.com/yourusername/your-repo-name'
    targetRevision: HEAD
  project: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
Apply this:

bash
Copy
Edit
kubectl apply -f argo-app.yaml
✅ Final Steps
Create a public GitHub repository scaffold:

Would you like me to generate this and give you the exact repo structure with README?

(Optional) Add CI for Go & Python Linting and Tests?

Would you like to run Go test / Python pytest automatically before pushing?

Let me know which of these next steps you'd like to proceed with first!
'''
