FROM cocoon/python
MAINTAINER cocoon

RUN apt-get update && apt-get clean
RUN apt-get install -q -y openjdk-7-jre-headless && apt-get clean
ADD http://mirrors.jenkins-ci.org/war/1.578/jenkins.war /opt/jenkins.war
RUN chmod 644 /opt/jenkins.war
ENV JENKINS_HOME /jenkins

ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt



# install robotframework uiautomator 
pip install -i https://pypi.binstar.org/pypi/simple robotframework-uiautomatorlibrary


ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]
EXPOSE 8080
CMD [""]