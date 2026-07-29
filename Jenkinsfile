pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Project Info') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version || true'
            }
        }

        stage('Docker Version') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build Completed') {
            steps {
                echo 'Travel Intelligence MLOps CI Pipeline Completed Successfully'
            }
        }
    }
}