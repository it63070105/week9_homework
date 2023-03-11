### Clone

```
git clone https://github.com/Tuchsanai/devpot_week9.git
```


### go to Directory
```
cd devpot_week9/Lab3

```




### Next, create a new file called Dockerfile in the root of your project directory with the following contents:
```
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

```

### build Docker image with docker build 
```
docker build -t fastapi-docker .
```

### Run the Docker container by executing the following command:
```
docker run -p 8087:80 fastapi-docker
```
