# kubecon-2026-eu-tutorial

# Install Tools
```bash
brew install kubectl
brew install kind
```

# Create Kind Cluster
```
kind create cluster --name kubecon-2026-eu-tutorial
```

# Verify Cluster
```
kubectl get nodes
kubectl get pods -A
```

