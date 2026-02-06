pipeline {
    agent any

    environment {
        APP_NAME = "Jenkins Python CI"
    }

    stages {

        stage('Show Environment') {
            steps {
                echo "Application: ${APP_NAME}"
            }
        }

        stage('Check Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'python hello.py'
            }
        }

        stage('List Workspace Files') {
            steps {
                bat 'dir'
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
