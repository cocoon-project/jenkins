jenkins
=======

jenkins docker image based on cocoon/python


on the docker host:

```
mkdir -p /home/cocoon/shared/jenkins
chmod 777 /home/cocoon/shared/jenkins
```


start the container

```
sudo docker run -p 8080:8080 -v /home/cocoon/shared/jenkins:/jenkins cocoon/jenkins
``