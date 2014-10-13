FROM cocoon/pyrun
MAINTAINER cocoon

RUN apt-get update && apt-get clean
RUN apt-get install -q -y git
RUN apt-get install -q -y openjdk-7-jre-headless && apt-get clean
ADD http://mirrors.jenkins-ci.org/war/1.578/jenkins.war /opt/jenkins.war
RUN chmod 644 /opt/jenkins.war
ENV JENKINS_HOME /jenkins



#ADD requirements.txt /tmp/
#RUN pip install -r /tmp/requirements.txt

# install robotframework uiautomator 
#RUN pip install -i https://pypi.binstar.org/pypi/simple robotframework-uiautomatorlibrary

# install droydrunner
#RUN pip install git+https://github.com/cocoon-project/droydrunner.git

# install pyjenkins
#RUN pip install PyYAML
#RUN pip install git+https://bitbucket.org/cocoon_bitbucket/pyjenkins.git

# volumes: /jenkins for the state , /tests for the test sources /opt/python for pyrun
#VOLUME /tests
#VOLUME /jenkins
#VOLUME /opt/python



ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]
EXPOSE 8080
CMD [""]