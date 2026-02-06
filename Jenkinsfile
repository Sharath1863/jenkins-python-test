pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-python-app"
        DOCKER_USER = "sharath2003"
        CONTAINER_NAME = "jenkins-python-container"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                bat 'pytest'
            }
        }

        stage('Run Python Script') {
            steps {
                echo 'Executing application script...'
                bat 'python hello.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Docker Login') {
            steps {
                echo 'Logging into Docker Hub...'
                withCredentials([usernamePassword(
                    credentialsId: '3151dacb-ae2c-4e95-b749-55dff8ad0643',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                }
            }
        }

        stage('Tag Docker Image') {
            steps {
                echo 'Tagging Docker image...'
                bat 'docker tag %IMAGE_NAME% %DOCKER_USER%/%IMAGE_NAME%'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing image to Docker Hub...'
                bat 'docker push %DOCKER_USER%/%IMAGE_NAME%'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                bat '''
                docker rm -f %CONTAINER_NAME% || exit 0
                docker run --name %CONTAINER_NAME% %IMAGE_NAME%
                '''
            }
        }
    }

    post {
        success {
            echo 'Docker CI/CD Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
