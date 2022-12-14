# Final-project-microservice
  -- Xuting Wu, Airu Song, Aohua Zhang, Zhengyao Pu

## Introduction
In the final project, we build a web microservice for users to query information of tech jobs. We provided some API for users to easily get what they want and they can also custimize that. And we also developed a user-friendly front-end to improve users' satisfaction level.

## Design Flow Diagram
#### This a containerized api(FastApi) deployed on AWS, which has continuous delivery feature.

![Figure](https://github.com/nogibjj/final-project-microservice-group/blob/main/picture.drawio.png)

## Dataset
#### Dataset source
https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries

#### Dataset table schema
![Figure](https://github.com/nogibjj/final-project-microservice-group/blob/main/data.png)
:height 10%
:width: 10%
:align: center

## Tools
Kaggle : Data source <br>
FastAPI : API development <br>
Databricks : could data storage <br>
AWS : auto deployment <br>
Pylint : format code

## Front-end Design
<img decoding="async" src="https://github.com/nogibjj/final-project-microservice-group/blob/main/front-end.png" width="50%" height="50%">

## API
1. Get the average salary of different levels in this position in the US from 2020-2022
    - /salaryofposition/{position}
2. Get average salary of this specific position in this specific country of all levels within the 3 years
    - /country/{country}/position/{position}
3. Get job title, company location, experience level by entering expected salary and year
    - salary/{salaryAmout}/year/{year}
4. Get Average salary of this the selected concurrency
    - /currency/{currency}
5. Get average salary for different company sizes given year, employment type, position title and level
    - /year/{year}/type/{emtype}/pos/{pos}/level/{level}

## Deployment

#### build docker image and run locally

```docker build .```  
```docker image ls```  
```docker run -p 127.0.0.1:8080:8080 453781e79c1a```  
#### build docker image and push to AWS ECR

```make build```

[![Deploy to ECR](https://github.com/nogibjj/final-project-microservice-group/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/final-project-microservice-group/actions/workflows/main.yml)
