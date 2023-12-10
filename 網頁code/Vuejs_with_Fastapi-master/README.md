# Vuejs_with_Fastapi

ITRI carbon emissions project demo with Vue and Fastapi.

- yml, Dockerfile: for Docker setup
- frontend: write with Vue3 & Typescript
- backend: write with Fastapi(Python)

### Backend: Fastapi
- Python environment
```
fastapi==0.82.0
joblib==1.1.0
pydantic==1.9.2
starlette==0.19.1
uvicorn==0.13.4
scikit-learn==1.1.2
```
- Dockerfile: set environment, running in port 5000
- src/main.py : router to deal with data
- src/models/*.pkl: put model to test (.pkl file)

### Frontend: Vuejs + TypeScript
- Vue3 with TypeScript
- Dockerfile: set environment, running in port 80



## Command to build docker image
```
docker-compose up -d --build
```
