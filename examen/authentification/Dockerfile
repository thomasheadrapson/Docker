# Dockerfile for Authentification tests

# Base Image
FROM ubuntu:18.04

# update, install pip, install flask and requests
RUN apt-get update && \
    apt-get install python3-pip -y && \
    pip3 install \
        flask==2.0.0 \
        requests

ADD ./authentification_test.py authentification_test.py


CMD ["python3", "authentification_test.py"]