pipeline {
    agent any

    environment {
        APP_NAME = "Jenkins Python CI"
        BUILD_ENV = "Development"
    }

    stages {

        stage('Show Environment Info') {
            steps {
                echo "Application: ${APP_NAME}"
                echo "Environment: ${BUILD_ENV}"
            }
        }

        stage('Check Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies (if any)...'
                bat 'pip install -r requirements.txt || echo No requirements file'
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

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
