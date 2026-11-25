
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-management-app:latest .'
            }
        }

        stage('Test Docker Container') {
            steps {
                sh '''
                    docker rm -f employee-test || true
                    docker run -d --name employee-test -p 5003:5000 employee-management-app:latest
                    sleep 5
                    docker ps
                    docker stop employee-test
                    docker rm employee-test
                '''
            }
        }
    }
}
