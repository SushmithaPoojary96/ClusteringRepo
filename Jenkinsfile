pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t customer-cluster .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker stop customer-app || true
                docker rm customer-app || true

                docker run -d \
                    --name customer-app \
                    -p 5000:5000 \
                    customer-cluster
                '''
            }
        }

        stage('Verify Container') {
            steps {
                sh 'docker ps'
            }
        }
    }
}