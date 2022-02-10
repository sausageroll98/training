# Local Kubernetes Deployment from Command Line

## Install tools

1. install "kubernetes-cli"

    ```cmd
    choco install kubernetes-cli -y
    ```

1. install "minikube"

     ``` cmd
    choco install minikube -y
    ```

## Setup local registry

> Terminal Tab 1 - "minikube"

1. Start the cluster with a 254 Ip range and allow insecure registries:
   
    ``` cmd
    minikube start --insecure-registry "10.0.0.0/24" --kubernetes-version=v1.23.2 --driver=docker
    ```

    Output of this type will be seen:

    ``` cmd

    🔎  Verifying Kubernetes components...
        ▪ Using image kubernetesui/metrics-scraper:v1.0.7
        ▪ Using image kubernetesui/dashboard:v2.3.1
        ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
    ╭──────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │                                                                                                      │
    │    Registry addon with docker driver uses port 50736 please use that instead of default port 5000    │
    │                                                                                                      │
    ╰──────────────────────────────────────────────────────────────────────────────────────────────────────╯
    📘  For more information see: https://minikube.sigs.k8s.io/docs/drivers/docker
        ▪ Using image registry:2.7.1
        ▪ Using image gcr.io/google_containers/kube-registry-proxy:0.4
    🔎  Verifying registry addon...
    🌟  Enabled addons: storage-provisioner, dashboard, default-storageclass, registry
    🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
    ```

    **Note**: The default port is currently set to `5000`.

2. Enable the registry `addon` within the Kubernetes cluster:

   ``` cmd
   minikube addons enable registry
   ```

3. Get the name of the registry pod, using the following regular expression:

    ``` cmd
    kubectl get pods --namespace kube-system  | findstr /R "\<registry-[^proxy]"
    ```

    This code finds the registry pods in the minikube instance, but excludes the registry proxy. In my example the name of the pod is `registry-jnrgw`

    Launch the `minikube` dashboard

    ```cmd
    minikube dashboard
    ```

    > Terminal Tab 2 - "port forward for container registry"
    
    Forward all traffic on port `5000` to our container registry

    ```cmd
    kubectl port-forward --namespace kube-system registry-jnrgw 5000:5000
    ```

    This shows the following output:

    ```cmd
    Forwarding from 127.0.0.1:5000 -> 5000
    Forwarding from [::1]:5000 -> 5000
    ```

    > Terminal Tab 3 - "Run container registry as interactive docker"

    ```cmd
    docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:host.docker.internal:5000"
    ```

    Expected output:

    ``` cmd
    Unable to find image 'alpine:latest' locally
    latest: Pulling from library/alpine
    59bf1c3509f3: Already exists
    Digest: sha256:21a3deaa0d32a8057914f36584b5288d2e5ecc984380bc0118285c70fa8c9300
    Status: Downloaded newer image for alpine:latest
    fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/APKINDEX.tar.gz
    fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/community/x86_64/APKINDEX.tar.gz
    (1/4) Installing ncurses-terminfo-base (6.3_p20211120-r0)
    (2/4) Installing ncurses-libs (6.3_p20211120-r0)
    (3/4) Installing readline (8.1.1-r0)
    (4/4) Installing socat (1.7.4.2-r0)
    Executing busybox-1.34.1-r3.trigger
    OK: 7 MiB in 18 packages
    ```

    The `minikube` container registry is now running, this can be checked by running:

    > Terminal Tab 4 - "Interaction"

    ``` cmd
    curl http://localhost:5000/v2/_catalog
    ```

    Expected output:

    ```cmd
    {"repositories":[]}
    ```

## Create the container image and upload to minikube registry

> Terminal Tab 4 - "Interaction"

1. Create a container image

    Start within the `hellokubrickfromkubernetes` folder

    Check the folder has the following files:
    * `Dockerfile`
    * `main.go`
    * `go.mod`
  
    ``` cmd
        dir
    ```

    Now build the docker image

    > Terminal Tab 4 - "Interaction"

    ``` cmd
    docker build . -t localhost:5000/hellokubrick:v1
    docker images
    ```

2. Upload image

    > Terminal Tab 4 - "Interaction"

   ```cmd
    docker push localhost:5000/hellokubrick:v1
    ```

    Validate the upload was successful:

    ``` cmd
        curl http://localhost:5000/v2/_catalog
    ```

    Expected output:

    ``` cmd
        {"repositories":["hellokubrick"]}
    ```

## Deploy Image on `minikube`

1. Create a kubernetes namespace for development called `hello-dev`

    > Terminal Tab 4 - "Interaction"

    ``` cmd
    kubectl create namespace hello-dev
    ```

    Confirmed with:

    ``` cmd
    kubectl get namespaces
    ```

1. Create pod for the image in the `hello-dev` namespace

    > Terminal Tab 4 - "Interaction"

    ``` cmd
    kubectl run hello-kubrick --image=localhost:5000/hellokubrick:v1 --port 8080 --namespace=hello-dev
    ```

    Confirmed with:

    ``` cmd
        kubectl get pods --namespace=hello-dev
    ```

    **NOTE** Using the namespace `hello-dev`

1.  Create a deployment for the image in the `hello-dev` namespace

    > Terminal Tab 4 - "Interaction"

    1. Our deployment will be called `hello-kubrick` for our tagged container:
        ``` cmd
        kubectl create deployment hello-kubrick --image=localhost:5000/hellokubrick:v1 --namespace=hello-dev
        ```
    1. Export a port for a `NodePort` to be our front end

        ```cmd
        kubectl expose deployment hello-kubrick --type=NodePort --port=8080 --namespace=hello-dev
        ```

        1. Check the network status

            > Terminal Tab 4 - "Interaction"

            ``` cmd
            kubectl get svc
            ```

        This shows a table of the networking for the kubernetes cluster

        |NAME|TYPE|CLUSTER-IP|EXTERNAL-IP|PORTS|AGE|
        |-|-|-|-|-|-|
        |hello-kubrick|NodePort|10.111.114.105|</none/>|8080:30983/TCP| 12m|

        1. Add Port mapping to the container
            > Terminal Tab 5 - "Application port mapping"

            ``` cmd
            kubectl port-forward service/hello-kubrick 1111:8080  --namespace=hello-dev
            ```

        1. Check the mapping is working

            From `localhost:1111` -> `minikube:8080` -> `container:8080`

            ``` cmd
            kubectl get svc --namespace=hello-dev
            ```

    1. Re-Run our curl command from earlier with our new `NodePort`

    > Terminal Tab 4 - "Interaction"

       Test by running:

       ``` cmd
           curl http://localhost:1111
       ```

1. Replace with `NodePort` with a `LoadBalancer`

    > Terminal Tab 5 - "Application port mapping"
    CTRL-C

    1. cleanup
        ``` cmd
kubeclt         get svc --namespace=hello-dev
        kubectl delete service hello-kubrick --namespace=hello-dev
        ```


    1. Create Loadbalancer

        > Terminal Tab 4 - "Interaction"

        ``` cmd
        kubectl expose deployment hello-kubrick --type=LoadBalancer --port=8080 --namespace=hello-dev
        ```

    1. Create minikube port mapping

        > Terminal Tab 5 - "Application port mapping"

        ``` cmd
        minikube tunnel
        ```

        > Terminal Tab 4 - "Interaction"

        ``` cmd
        kubectl get svc  --namespace=hello-dev
        ```

        |NAME|TYPE|CLUSTER-IP|EXTERNAL-IP|PORTS|AGE|
        |-|-|-|-|-|-|
        |hello-kubrick|LoadBalancer|10.107.194.7|127.0.0.1|8080:30410/TCP| 12m|

    1. Test the url by running:

        ``` cmd
        curl http://localhost:8080
        ```

---

## Pod scaling 

> Terminal Tab 4 - "Interaction"
1. Retrieve the current `replicaset` value

    ```cmd
    kubectl get replicaset --namespace=hello-dev
    ```

1. Change the scaling to 10

    ``` cmd
    kubectl scale --replicas=10 deployment/hello-kubrick --namespace=hello-dev
    ```

1. re-run curl commands

    ``` cmd
        curl http://localhost:8080
    ```

1. Change the scaling back to 1

    ``` cmd
        kubectl scale --replicas=1 deployment/hello-kubrick --namespace=hello-dev
    ```

1. Test the url by running:

    ``` cmd
        curl http://localhost:8080
    ```
