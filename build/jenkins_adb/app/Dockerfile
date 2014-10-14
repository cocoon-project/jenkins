FROM cocoon/jenkins
MAINTAINER cocoon

# install more lib for uiautomator
ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt


##################################
# install ADB
#

# Stop debconf from complaining about missing frontend
ENV DEBIAN_FRONTEND noninteractive

# setup
RUN apt-get update && apt-get clean


# 32-bit libraries and build deps for ADB
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get -y install libc6:i386 libstdc++6:i386 && \
    apt-get -y install wget unzip

# Install ADB
RUN wget --progress=dot:giga -O /opt/adt.zip \
      http://dl.google.com/android/adt/adt-bundle-linux-x86_64-20140702.zip && \
    unzip /opt/adt.zip adt-bundle-linux-x86_64-20140702/sdk/platform-tools/adb -d /opt && \
    mv /opt/adt-bundle-linux-x86_64-20140702 /opt/adt && \
    rm /opt/adt.zip && \
    ln -s /opt/adt/sdk/platform-tools/adb /usr/local/bin/adb

# Set up insecure default key
RUN mkdir -m 0750 /.android
ADD files/insecure_shared_adbkey /.android/adbkey
ADD files/insecure_shared_adbkey.pub /.android/adbkey.pub

# Clean up
RUN    apt-get clean && \
    rm -rf /var/cache/apt/*



