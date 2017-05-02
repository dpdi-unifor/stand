FROM ubuntu:16.04
MAINTAINER Vinicius Dias <viniciusvdias@dcc.ufmg.br>

# Install python and jdk
RUN apt-get update \
   && apt-get install -qy python-pip

# Install juicer
ENV STAND_HOME /usr/local/stand
RUN mkdir -p $STAND_HOME/conf
RUN mkdir -p $STAND_HOME/sbin
RUN mkdir -p $STAND_HOME/stand
ADD sbin $STAND_HOME/sbin
ADD stand $STAND_HOME/stand

# Install juicer requirements and entrypoint
ADD requirements.txt $STAND_HOME
RUN pip install -r $STAND_HOME/requirements.txt
EXPOSE 5000
CMD ["/usr/local/stand/sbin/stand-daemon.sh", "startf"]
