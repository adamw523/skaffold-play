# skaffold-play
Playing around with Skaffold


# Notes for meetup

```

# change context
kubectl config use-context my-cluster-name

# set current context
kubectl config set current-context docker-desktop

# set current namespace
kubectl config set-context --current --namespace=skaffold-play

# create a namespace
kubectl create namespace skaffold-play

# running dev
skaffold dev --port-forward

# run busy
kubectl run busy --image busybox  -it --generator=run-pod/v1

# manual port forward
kubectl port-forward svc/web-service 8000:8000

```
