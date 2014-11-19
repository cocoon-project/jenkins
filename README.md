jenkins
=======

jenkins docker image based on cocoon/base

* + robotframwork
* + pyjenkins
* + droydrunner client



play with the image in a sandbox


```
docker run -d -8020:8080 cocoon/jenkins

```


open a browser at ${docker_host}:8020




composition
========
debian:wheezy
	cocoon/base
		cocoon/jenkins


