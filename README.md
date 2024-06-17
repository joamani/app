# webapp

## Description
A simple web application that prints the origin public IP of any request in reverse and stores it in a database.

## Setup

### Prerequisites
- Python 3.9
- Docker
- Helm
- Kubernetes (AWS)

### Running Locally

1. Install dependencies:
   ```bash
   pip install Flask sqlite3
   
2. Run the application:
   python app.py

3. Access the application at http://localhost.

Docker
1. Build Docker image:
   docker build -t app .
2. Run Docker container:
   docker run -p 80:80 my-flask-app

Helm
1. create helm:
   helm create app

CI/CD
Set up GitHub Actions with secrets for DockerHub credentials.
Push to GitHub and the CI/CD pipeline will build, push, and deploy the application.

Access the Deployed Application
URL: [Your AWS URL]
