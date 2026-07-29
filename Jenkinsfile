pipeline {

    agent any


    stages {


        stage('Clone Code') {
            steps {
                git 'https://github.com/SushmithaPoojary96/ClusteringRepo.git'
            }
        }


        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t customer-cluster .
                '''
            }
        }


        stage('Run Docker Container') {
            steps {
                sh '''
                docker stop customer-app || true
                docker rm customer-app || true

                docker run -d \
                -p 5000:5000 \
                --name customer-app \
                customer-cluster
                '''
            }
        }


        stage('Verify Container') {
            steps {
                sh '''
                docker ps
                '''
            }
        }
    }
}