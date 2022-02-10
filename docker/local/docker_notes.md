# Docker

- Docker is a platform for developing, deploying and running applications
- Applications can be packaged and they are run in containers
- Containers can be run in any machine where Docker is installed

## Docker benefits

- No compatability issues
- Easy to maintain and deploy applications
- Consistent behaviour

## Docker terminology
**Docker images** A docker image is a template to build containers. Typically contains the OS, application and the supporting packages to be deployed.

**Docker containers** An isolated environment that runs applications. Containers can be built from docker images.

**Dockerfile** A script containing instructions to create a dockee image.

**Docker daemon** A process that manages docker containers. We will communicate with the daemon using the Command Line Interface (CLI)

**Docker Registry** A place where the docker images are stored. Examples include:
- Docker Hub
- Amazon ECR
- Azure Container Registry

## How does Docker work?


## Docker basic commands
View the docker help menu
> \> docker --help

View the docker help menu for a particular command
> \>docker \<COMMAND> --help
> \>docker images --help
> \>docker container --help

## Example: Docker Hello World

In this section, we will pull the Hello World image from Docker Hub and run it

View all the images present in our system
> \>docker image ls

View all the running containers present in our system
> \>docker container ls

View all the containers (running and stopped) in our system
> \>docker container ls -a

Pull down the hello-world image and run it
> \>docker pull hello-world
> \>docker run hello-world

Now, if you view all the images using the comman `docker image ls` as above, you will notice the "hello-world" image added to the loist.

The docker images each have a unique id `IMAGE ID` and a tag `TAG` (which correponds to the version of the image)

Also, if you view all the containers `docker container ls`, you will notice that each container has a unique container id `CONTAINER ID`, a randomly generated name `NAMES` and the image on which the container is based upon.

Removing a Docker image
> \>docker rmi \<IMAGE ID>
Sometimes, the above command can result in an error: `Error response from daemon: conflict: unable to delete feb5d9fea6a5 (must be forced) - image is being used by stopped container c250dc98fdae`

This means that you first have to remove the container that uses the reference image before deleting the image.

Removing a Docker container
> \>docker rm \<CONTAINER ID>
or
> \>docker rm \<CONTAINER NAME>

Removing all stopped containers
> \> docker container prune
## Example: Creating a Docker image with ubuntu and install miniconda

First, we need to pull the ubuntu image from Docker hub

> \>docker pull ubuntu

Next, we run the docker image with an interactive terminal for bash shell

> \>docker run -it ubuntu

The `-it` flag allows you to run containers in an interactive mode with access to a shell. This will open a bash shell inside your Docker container which would look different to your powershell prompt (something like `root@xxxxxxxx:/#`)

On order to install miniconda, we use the `wget` tool. But first, we need to install `wget` using the Advanced Package Tool (apt)

The following comman updates the apt package manager
> \# apt update

Following this, we install `wget`
> \# apt install wget

To check if `wget` is successfully instealled,
> \# wget --version

Use wget to download miniconda
> \# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

Check if miniconda installer file has been downloaded in your current directory
> \# ls

Install miniconda using the following command

> \# bash Miniconda3-latest-Linux-x86_64.sh -b

To check which directory you are currently in
> \# pwd

To navigate to the miniconda installation folder
> \# cd /root/miniconda3
> \# ls

Currently, conda is not available in the default path environment variable. To check this we can do
> \# echo $PATH

To add conda to the PATH, we do
> \# export PATH="/root/miniconda3/bin:$PATH"

Before you run conda commands, you have to initialise it in the bash shell.

> \# conda init bash

To check if conda command works
> \# conda --version

Check versions of all conda programs
> \# conda list

Exit the container to get back to the Powershell prompt 
> Ctrl+P Ctrl+Q (This will keep the container running in the background while exiting)
> Ctrl+D (This will stop the container before exiting)

You can reconnect to a running container again by using `docker attach`
> \> docker attach \<CONTAINER ID>

The above command only works for running containers. For stopped containers you first have to start them before attaching.
> \> docker start \<CONTAINER ID>
> \> docker attach \<CONTAINER ID>

Commit this container as a new Docker image (a new template that includes Ubuntu + wget + miniconda)
> \> docker commit \<CONTAINER ID\>

Run `docker image ls` to see if a new image has been created with name \<none\>. Note the `IMAGE ID` for this image. 

Tag this image with a descriptive name
> \> docker tag \<IMAGE ID\> \<IMAGE NAME\>:\<TAG\>  
> \> docker tag 9599329aa62d ubuntu_miniconda:latest

This new image can now be used as a template to create new containers that has Ubuntu, wget and miniconda pre-installed in them.

## Example: Creating a Docker image with ubntu and miniconda using a Dockerfile
Steps taken to create the image in the above example:
- Download the ubuntu image
- install wget
- Download and install miniconda
- Add miniconda to path
- Initialise the conda shell

We create a dockerfile (which is just like a text file) with some commands to execute the above steps. For more information on Dockerfile commands, see <https://docs.docker.com/engine/reference/builder/>

```dockerfile
# Download the ubuntu image
FROM ubuntu

# Install wget
RUN apt update
RUN apt install -y wget

# Download and install miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b

# Add miniconda to PATH
ENV PATH="/root/miniconda3/bin:$PATH"

# Initialize the conda shell
RUN conda init bash
```
Save the above code snippet as ubuntu_miniconda_df.dockerfile.


To build a Docker image using this Dockerfile, we run the following command:
> \> docker build -f \<Dockerfile\> -t \<IMAGE NAME\> .

For example,
> \> docker build -f ubuntu_miniconda_df.dockerfile -t ubuntu_miniconda_df .

This will create a new Docker image `ubuntu_miniconda_df` from this Dockerfile.

## Example: Deploying a Flask app inside a Docker container manually

Steps to run a flask app inside a Docker container

- Use the ubuntu_miniconda_df image to create a container
- Install Flask and Waitress
- Copy the python script containing the flask app from the host machine into the container
- Commit this container as a new image called flask_app
- Run the flask app from inside a container created from this image `flask_app` by also mapping the ports from host to container
- View the flask app on our browser in the host machine

Use the ubuntu_miniconda_df image to create a container
> \> docker run -it ubuntu_miniconda_df

Install flask and waitress
> \# conda install -y flask waitress

Note: Use `-y` to automatically install without prompt for user

To copy files from host computer to docker container, we first have to detach from the container without stopping it by doing `Ctrl+P Ctrl+Q`

To copy the folder, we use the following command:
> \> docker cp \<host_machine_path\> \<CONTAINER ID\>:\<container_path\>

For example,
> \> docker cp .\hello_flask_app\ bc702481a6b3:/

You can check if the folder and Python file inside it has been copied into the container by attaching to the container and navigating to the correct directory.

Commit this container with the flask app as a new Docker image called `flask_app`
> \> docker commit bc702481a6b3 flask_app

Let's create a new container from this image `flask_app` that we created
> \> docker run -it -p \<HOST_PORT\>:\<CONTAINER_PORT\> flask_app  
> \> docker run -it -p 5000:5050 flask_app

Inside the container, navigate to the folder where your Python file is located.
> \# cd hello_flask_app/

Run the waitress server to serve the app on the container port
> \# waitress-serve --host=0.0.0.0 --port=5050 hello_flask:app

This will show a message that the app is served on the given host and port. 

Now, we can access it from the host machine's browser by going to <http://127.0.0.1:HOST_PORT>

You should see a message, "Hello flask from inside Docker container id `CONTAINER ID`"

## Example: Deploying a flask app inside a Docker container using a Dockerfile

- Use the ubuntu_miniconda_df as the base Docker image
- Install flask and waitress
- Copy the python script containing the flask app from our host machine into the container
- Change the directory to flask_app
- Run the waitress-serve command to serve the app

```Dockerfile
# Use the ubuntu_miniconda_df as the base image
FROM ubuntu_miniconda_df

# Install flask and waitress
RUN conda install -y flask waitress

# Copy the flask app from host to container
COPY ./hello_flask_app /hello_flask_app

# Change the directory to the hello_flask_app folder
WORKDIR /hello_flask_app

# Run the waitress-serve command
CMD ["waitress-serve","--host=0.0.0.0","--port=5050","hello_flask:app"]
```

Save the above code snippet as `flask_app_df.dockerfile`.

To build a Docker image using this Dockerfile, we run the following command:
> \> docker build -f \<Dockerfile\> -t \<IMAGE NAME\> .

For example,
> \> docker build -f flask_app_df.dockerfile -t flask_app_df .

This will create a new Docker image `flask_app_df` from this Dockerfile.

Now, you can fire up one of more docker containers using this command:
> \> docker run -it -d -p \<HOST_PORT\>:5050 flask_app_df

Note: `-d` flag indicates that the container starts in detached mode (running in background)

Depending on the host port for each container, you can go to the browser and view it to see the corresponding container id from which the app is running.

## Exercise: Start from Python Slim image and run this flask app using Dockerfile

Create a dockerfile with the following steps

- Use the base image Python:3.8.12-slim 
- Install flask and waitress using pip
- Copy the flask app into the image
- Change the working directory to the flask app
- Run the waitress-serve command

Using this dockerfile, build a new image and save it as `flask_app_python_slim`

Run a container using this newly created image, map the port 5035:5050 and check if you can see this app from your browser with the corresponding container id.

## Pushing your docker image to docker hub

You can push your Docker image, e.g. `flask_app_df` to your docker hub account by first tagging it as `<ACCOUNT_NAME>/<IMAGE_NAME>:<TAG>` and then using `docker push` command.