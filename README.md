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


## Tools
Kaggle : Data source <br>
FastAPI : API development <br>
Databricks : could data storage <br>
AWS : auto deployment <br>
Pylint : format code


## API
1. First item
2. Second item
3. Get job title, company location, experience level by entering expected salary and year
    - salary/{salaryAmout}/year/{year}
4. Fourth item

#### build docker image and run locally

```docker build .```  
```docker image ls```  
```docker run -p 127.0.0.1:8080:8080 453781e79c1a```  
#### build docker image and push to AWS ECR

```make build```
