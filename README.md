# Delivery Fee Calculator API

My implementation for Wolt 2024 engineering internship: Backend

## Description
Single endpoint API that calculates delivery fee. Built with Python3.10 and FastAPI

### Running with docker
At the root folder containing the docker-compose.yml run
```
docker compose up
```
* head to http://localhost:8080/docs

there you can test the api with OpenAPI docs.

#### Testing with docker
While the docker compose from previous command is still running, run command
```
docker exec -it wolt-app sh -c "pytest test/deliveryFeeTest.py"
```

#### Code style lint with docker
to run style linter run 
```
docker exec -it wolt-app sh -c "pycodestyle src -v"
```

### Running locally
#### dependencies
* python3.10
* virtualenv suggested but optional

to install python packages, in app folder run
```
pip install -r requirements.txt
```
#### Run server
in app folder run
```
uvicorn src.main:app --host 0.0.0.0 --port 8080
```
* head to http://localhost:8080/docs

#### Run tests
in app folder run
```
pytest test/deliveryFeeTest.py
```

#### Run pycodestyle
in app folder run

```
pycodestyle src -v
```
