# Kubernetes deploy step-by-step

Creating a local cluster:
```shell
$ minikube start
```
 Build docker image of you application
```shell
$ docker build -t dandaniel/tcc .
```
 (Optional) Run it in a container
```shell
$ docker run --rm -p 8080:8080 danliberato/tcc
```
 Push the image to DockerHub (or other container registry)
```shell
$ docker push dandaniel/tcc
```
 Apply k8s configuration to the image
```shell
$ minikube kubectl -- apply -f tcc.yaml 
```
 Check the online pods
```shell
$ minikube kubectl -- get pods -A
```
 Forward local port to the k8s container
```shell
$ minikube kubectl -- port-forward pod/tcc 8080:8080
```

Access you application with browser (localhost:8080/docs)

### Open dashboard
```shell
$ minikube dashboard
```
