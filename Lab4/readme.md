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

Next, create a new file called main.py in the root of your project directory with the following contents:

```
from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel

app = FastAPI()

class ImageData(BaseModel):
    caption: str

@app.post("/uploadimage")
async def upload_image(image_data: ImageData, file: UploadFile = File(...)):
    return {"filename": file.filename, "caption": image_data.caption}

```