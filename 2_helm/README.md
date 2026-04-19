# Package Management with Helm

## Prerequisites
follow `../0_docker/README.md` to set up the docker image
follow `../1_kubernetes/README.md` to set up the kind cluster
`cd ../2_helm`

## Install Helm
```
brew install helm
```

## Create a Helm Chart
```
helm create hello-world
```

## Deploy the Helm Chart
```
helm install hello-world ./hello-world
```

## Verify app is running
```
kubectl port-forward service/hello-world 8080:80
```

## Modify helm chart to serve custom image

### Replace values.yaml
```
mv values.yaml hello-world/values.yaml
```

### Load the docker image into the kind cluster
```
kind load docker-image hello-world:latest --name kubecon-2026-eu-tutorial
```

### Deploy the Helm Chart with new values
```
helm upgrade hello-world ./hello-world --values ./hello-world/values.yaml
```

## Verify app is running
```
kubectl port-forward service/hello-world 8080:5000
```