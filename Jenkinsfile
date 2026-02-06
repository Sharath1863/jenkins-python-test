pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning source code from GitHub...'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'python hello.py'
            }
        }

        stage('Build Status') {
            steps {
                echo 'Pipeline executed successfully!'
            }
        }

    }
}
