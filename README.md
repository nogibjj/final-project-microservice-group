# Final-project-microservice
  -- Xuting Wu, Airu Song, Aohua Zhang, Zhengyao Pu

## Introduction
In the final project, we build a web microservice for users to query information of tech jobs. We provided some API for users to easily get what they want and they can also custimize that. And we also developed a user-friendly front-end to improve users' satisfaction level.

## Design Flow Diagram
#### This a containerized api(FastApi) deployed on AWS, which has continuous delivery feature.

![Figure](https://github.com/nogibjj/final-project-microservice-group/blob/main/picture.drawio.png)

## Front-end Design

## Dataset
#### Dataset source
https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

#### Dataset table schema
![Figure](https://github.com/nogibjj/final-project-microservice-group/blob/main/data.png)

## API Details
```


## Deployment

#### build docker image and run locally

```docker build .```  
```docker image ls```  
```docker run -p 127.0.0.1:8080:8080 453781e79c1a```  
#### build docker image and push to AWS ECR

```make build```
