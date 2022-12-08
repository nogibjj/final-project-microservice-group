# final-project-microservice
## This a containerized api(FastApi) deployed on AWS, which has continuous delivery feature.
## run  
### build docker image and run locally
```docker build .```  
```docker image ls```  
```docker run -p 127.0.0.1:8080:8080 453781e79c1a```  
### build docker image and push to AWS ECR
```make build```