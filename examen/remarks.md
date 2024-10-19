## Introduction

This is a description of the project deliverable for the Docker module.

In addition to the four test deliverables a test for the status route is also included
* initial reason was to build a basic, precursor test design for the simplest case/route, on which to then build the deliverable test cases, 
* has been included in delivred project to illustrate the design process, and for completeness, i.e. all routes tested.



## Directory structure

In the project home directory the following are found
* this remarks markdown file
* curls.md markdown file with some example Curl API calls
* the project docker-compose file
* the setup.sh script file that calls docker engine to build the images and setup the services using the docker-compose file
* the tests results log, api_test.log



All files specific to each of the test sets are kept in their own separate sub-directory of the project directory (status, authentification, authorization, content)
* these directories are used to separate dockerfiles for each test set,
* it is logical to also separate code files for each test set into the relevant sub-directory



## Dockerfiles

These all follow the same model, being

FROM - use the docker ubuntu version 18.04

RUN - install updates and packages

ADD - copy the test python file from its host project subdirectory

CMD - run the python test file



## Docker Compose


Five services are defined.
* sentiment - the API app

and the four test sets

* status, authentification, authorization, content

These five services all share the same network, named sentimentnw

The four test services share a volume, bound to the host project directory, where they write to the log file, api_test.log.
Each test service defines the environment variable LOG. Is there a more elagent way to do this

The five services are chained using the "depends_on" parameter to schedule the test services one after the other and all of those after the API service.
* all the test services depend on the API service being active, so the first test service, status, has the api service as the argument for this parameter.
* the other test services are chained using the previous test service as the argument for this parameter - this is done to ensure the proper separation by test group of the test results when outputing the results (to the api_test.log file)
* for example, the second test service, authentification, is scheduled after the first, status, by having that test service as the argument for this parameter, by

        depends_on:
            status:
                condition: service_completed_successfully
    

The environment variable LOG 
* is specified in the setup.sh script file,
* is accessed in the docker_compose file in the "environment" section for each test service, by

        environment:
            LOG: ${LOG}

* which passes this variable to the container as an environment variable internal to the container of the test service.


The build commands in setup.sh can be transfered to the docker compose file by using the "build" and "pull_policy:build" options for each service.
These are included in the compose file but are commented out because it was specified to include docker build commands in the setup.sh script file. 