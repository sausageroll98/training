# Ducktales

## Create `base64`  values

### PowerShell

```pwsh
[System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("Donald"))
```

### Bash

```bash
echo 'Donald'| base64
```

---
## Create the `ducktales` container

1. Create and push local container

    ```cmd
    docker build . -t localhost:5000/ducktales:v1
    docker push localhost:5000/ducktales:v1
    ```

1. Test container contents

    ```cmd
    curl http://localhost:5000/v2/_catalog
    ```

## create an environment

This is targetted for `dev` - but can be repeated for:

 * `dev`
 * `test`
 * `prod`

``` cmd
kubectl create namespace ducktales-dev
```

or

```cmd
kubectl apply -f dev/namespace.yaml 
```

### apply secrets for environment, e.g. `dev`

``` cmd
kubectl apply -f dev/secrets.yaml
```

### deploy and service

``` cmd
kubectl apply -f dev/deployment.yaml
kubectl apply -f dev/service.yaml
```

## To test

Port forward and curl

```cmd
kubectl port-forward service/ducktales-dev 8100:8100  --namespace=ducktales-dev
curl http://localhost:8100

```
---

### Create a `test` environment

1. For test combine the YAML files into one

    ```cmd
    kubectl apply -f ./test.yaml 
    ```

    **NOTE* to delete the whole namespace

    ``` cmd
    kubectl delete -f ./test.yaml
    ```

1. check all the kubectl services are running

    ```cmd
    minikube service list
    ```

1. port forward and test

    ```cmd
    kubectl port-forward service/ducktales-test 8101:8101  --namespace=ducktales-test
    curl http://localhost:8101

    ```

### Create a `prod` denvironment

Doing a rolling upgrade on prod

The following will be added to the `yaml` to allow for updates
```
    strategy:
        type: RollingUpdate
        rollingUpdate:
          maxUnavailable: 1
          maxSurge: 1

```

1. Create a container with the docker tag `localhost:5000/ducktales:prod`

    ```cmd
    docker build . -t localhost:5000/ducktales:prod
    docker push localhost:5000/ducktales:prod
    ```


1. Create the `prod` enviroment

    This time we are allowing the environment to be updated by adding `--force=true --grace-period=0` parameters

    ``` cmd
    kubectl apply -f .\prod.yaml --force=true --grace-period=0
    ```

1. Make a change to the code/container

    Create a new container with the docker tag `localhost:5000/ducktales:prod`

    ```cmd
    docker build . -t localhost:5000/ducktales:prod
    docker push localhost:5000/ducktales:prod
    ```

1. Apply the update to Kubernetes

    ``` cmd
    kubectl apply -f .\prod.yaml --force=true --grace-period=0
    ```

1. Enable port forwarding
 
    > In a separate shell

    ``` cmd
    kubectl port-forward service/ducktales-prod 8102:8101  --namespace=ducktales-prod
    ```

1. Test the `prod` instance

    ``` cmd
    curl http://localhost:8102
    ```

## Rolling Update

1. Perform the rolling update

    ``` cmd
    kubectl rollout restart deployment ducktales-prod --namespace=ducktales-prod
    ```

1. Check the rollout status

    ``` cmd
        kubectl rollout status deployment ducktales-prod --namespace=ducktales-prod 
    ```

1. Restart the port forwarding

    ``` cmd
    kubectl port-forward service/ducktales-prod 8102:8101  --namespace=ducktales-prod
    ```

1. Test the update to `prod`

    ``` cmd
    curl http://localhost:8102
    ```
##  Example change to load balancer for prod

1. Remove the old instance

    ``` cmd
    kubectl delete -f .\prod.yaml --force=true --grace-period=0
    ```

1. Change config from `NodePort` to `LoadBalancer` in the YAML


1. Re-add kubernetes for `ducktales-prod`

    ``` cmd
    kubectl apply -f .\prod.yaml --force=true --grace-period=0
    ```

1. Run via minikube tunnel

    ``` cmd
    minikube tunnel
    ```

1. Validate the load bnalancer

    ``` cmd
    curl http:/127.0.0.1:8101
    ```
