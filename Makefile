install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:	
	black *.py dblib/*py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py dblib

build:
	# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 501033498090.dkr.ecr.us-east-1.amazonaws.com
	aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/w8g8w9j5
	# docker build -t proj4 .
	docker build -t final .
	# docker tag proj4:latest 501033498090.dkr.ecr.us-east-1.amazonaws.com/proj4:latest
	docker tag final:latest public.ecr.aws/w8g8w9j5/final:latest
	# docker push 501033498090.dkr.ecr.us-east-1.amazonaws.com/proj4:latest
	docker push public.ecr.aws/w8g8w9j5/final:latest

all: install lint test