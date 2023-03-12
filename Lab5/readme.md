### Clone

```
git clone https://github.com/Tuchsanai/devpot_week9.git
```


### go to Directory
```
cd devpot_week9/Lab5

```




### Next, create a new file called Dockerfile in the root of your project directory with the following contents:
```
FFROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

### build Docker image with docker build 
```
docker build -t fastapi-docker_lab5 .
```

### Run the Docker container by executing the following command:
```
docker run -p 8088:80 fastapi-docker_lab5 
```
