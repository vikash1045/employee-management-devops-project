# Employee Management System – DevOps CI/CD Project

## 📌 Project Overview

The Employee Management System is a web-based application developed using Python Flask and PostgreSQL. It allows users to manage employee records through a simple dashboard.

This project demonstrates DevOps practices including GitHub version control, Docker containerization, Jenkins CI/CD pipeline, PostgreSQL database integration, and cloud deployment using Render.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| PostgreSQL | Database |
| Neon | Cloud PostgreSQL hosting |
| HTML, CSS, JavaScript | Frontend |
| Docker | Application containerization |
| Jenkins | CI/CD automation |
| Git & GitHub | Version control |
| Render | Cloud deployment |

## ✨ Application Features

- View employee records
- Add new employees
- Delete employee records
- Employee management dashboard
- PostgreSQL database integration

## ⚙️ DevOps Implementation

### 1. Source Code Management
Used Git and GitHub to manage and maintain application source code.

### 2. CI/CD Pipeline
Created a Jenkins pipeline to automate:
- Checkout Code
- Build Docker Image
- Run Tests

### 3. Docker Containerization
Created a Dockerfile to build and run the Flask application inside a Docker container.

### 4. Database Integration
Integrated Neon PostgreSQL to store and manage employee information.

### 5. Cloud Deployment
Deployed the Flask application on Render and connected it to the Neon PostgreSQL database.

## 🏗️ Project Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
Jenkins CI/CD Pipeline
    |
    v
Docker Build & Test
    |
    v
Render Cloud Deployment
    |
    v
Flask Web Application
    |
    v
Neon PostgreSQL Database
```

## 📂 Project Structure

```text
employee-management-devops-project/
│
├── templates/
│   └── index.html
│
├── app.py
├── Dockerfile
├── Jenkins.Dockerfile
├── Jenkinsfile
├── requirements.txt
├── .dockerignore
└── .gitignore
```

## 🔗 Project Links

**GitHub Repository:**

https://github.com/vikash1045/employee-management-devops-project

**Live Application:**

https://aws-devops-cicd-project-1.onrender.com

## 🎯 Learning Outcomes

- Developed a Flask-based web application.
- Integrated PostgreSQL using Neon.
- Implemented Docker containerization.
- Configured Jenkins CI/CD pipeline.
- Managed source code using Git and GitHub.
- Deployed a web application using Render.

## 👨‍💻 Author

**R. Padmavikash**

GitHub: https://github.com/vikash1045
