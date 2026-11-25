pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vikash1045/aws-devops-cicd-project.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Employee Management Application'
                sh 'ls -la'
            }
        }

        stage('Test') {
            steps {
                sh 'test -f app.py'
                sh 'test -f Dockerfile'
                sh 'test -f requirements.txt'
                echo 'All project files verified successfully!'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t employee-management-app:${BUILD_NUMBER} .'
                sh 'docker tag employee-management-app:${BUILD_NUMBER} employee-management-app:latest'
            }
        }

        stage('Complete') {
            steps {
                echo 'CI/CD Pipeline completed successfully!'
            }
        }
    }
}