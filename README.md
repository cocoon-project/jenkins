jenkins
=======

jenkins docker image based on cocoon/pyrun


play with the image in a sandbox


```
docker run -d -P cocoon/jenkins

```

check the jenkins httpports


```
docker ps


CONTAINER ID        IMAGE                     COMMAND                CREATED             STATUS              PORTS                     NAMES
9f7923d2f679        cocoon/jenkins:latest     java -jar /opt/jenki   7 seconds ago       Up 5 seconds        0.0.0.0:49154->8080/tcp   drunk_hopper
```

open a browser at ${docker_host}:49154




customizing jenkins
volumes:

/jenkins : the place where jenkins store its state
/tests   : the place to store te test you want to run
/opt/python : the python environment ( pyrun )








composition
========
debian:wheezy
	cocoon/python
		cocoon/jenkins



on the docker host:

```
mkdir -p /home/cocoon/shared/jenkins
chmod 777 /home/cocoon/shared/jenkins

mkdir -p /home/cocoon/shared/robot
chmod 777 /home/cocoon/shared/robot


```


start the container

```
sudo docker run -p 8080:8080 -v /home/cocoon/shared/jenkins:/jenkins -v /home/cocoon/shared/robot:/robot    cocoon/jenkins
```

/jenkins : the state for the jenkins container

/robot : the robotframwork test sources