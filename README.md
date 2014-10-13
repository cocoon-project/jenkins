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
```

open a browser at ${docker_host}:49153




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