# week9_homework

```
- git clone https://github.com/it63070105/week9_homework.git
- cd week9_homework
- cd backend
- docker build -t wk9-backend .
- cd ..
- cd frontend
- docker build -t wk9-frontend .
- cd ..
- docker run -d -p 8088:80 wk9-backend
- docker run -p 8081:8081 wk9-frontend
```
