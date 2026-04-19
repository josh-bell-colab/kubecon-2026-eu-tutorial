## Prerequisites
follow `../0_docker/README.md` to set up the docker image
follow `../1_kubernetes/README.md` to set up the kind cluster

# Install argo
```
ARGO_WORKFLOWS_VERSION="v4.0.4"
kubectl create namespace argo
kubectl apply --server-side -n argo -f "https://github.com/argoproj/argo-workflows/releases/download/${ARGO_WORKFLOWS_VERSION}/quick-start-minimal.yaml"
kubectl -n argo port-forward service/argo-server 2746:2746
```

Install argo CLI
```
brew install argo
```

# Access Argo Workflows UI
Open your browser to `https://localhost:2746` and accept the self-signed certificate.

# Use Argo Workflows to deploy a simple application
```
argo submit -n argo ./3_argo_workflows/hello-world.yaml --watch
```

# Cleanup
`kind delete cluster --name kubecon-2026-eu-tutorial`