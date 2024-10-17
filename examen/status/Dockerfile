# Dockerfile for Status tests

# Base Image
FROM ubuntu:18.04

# update, install pip, install flask and requests
RUN apt-get update && \
    apt-get install python3-pip -y && \
    pip3 install \
        flask==2.0.0 \
        requests

        
ADD ./status_test.py status_test.py


CMD ["python3", "status_test.py"]