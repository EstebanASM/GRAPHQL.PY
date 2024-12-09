# GRAPHQL.PY


## Description
This is a simple Python application using FastAPI and Strawberry for GraphQL, running on an HTTP server powered by Uvicorn. This program presents a small GraphQL API that returns a list of movies with their titles and directors.

## Project Links
- **Docker Hub Repository**: [estebanandres/fastapi-strawberry-app on Docker Hub](https://hub.docker.com/repository/docker/estebanandres/fastapi-strawberry-app/general)

## Getting Started

### Cloning the Repository
To clone the repository, use the following command:
```bash
git clone https://github.com/EstebanASM/GRAPHQL.PY.git
```
Navigate to the project directory:
```bash
cd GRAPHQL.PY
```

### Running the Application Locally (Without Docker)
#### Prerequisites
- [Python](https://www.python.org/downloads/) must be installed on your machine.
- Install FastAPI, Strawberry, Uvicorn, and GraphQL dependencies:
   ```bash
   pip install requirements.txt
   ```

#### Running the Application
1. Inside the project directory, start the server with:
   ```bash
   python main.py
   ```
2. We access the application in our browser
   ```
   http://localhost:8000
   ```
3. We enter the following link to access the GraphQL interface and be able to make our requests
   ```
   http://localhost:8000/graphql
   ```

### Running the Application with Docker

To run the application with Docker, visit the Docker Hub repository for this project: [estebanandres/fastapi-strawberry-app on Docker Hub](https://hub.docker.com/repository/docker/estebanandres/fastapi-strawberry-app/general).
