jenkins
=======

jenkins docker image based on cocoon/python


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
``