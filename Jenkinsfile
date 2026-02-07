pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-python-app"
        DOCKER_USER = "sharath2003"
        CONTAINER_NAME = "jenkins-python-container"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh """
                docker build -t ${DOCKER_USER}/${IMAGE_NAME}:${IMAGE_TAG} .
                docker tag ${DOCKER_USER}/${IMAGE_NAME}:${IMAGE_TAG} ${DOCKER_USER}/${IMAGE_NAME}:latest
                """
            }
        }

        stage('Docker Login') {
            steps {
                echo 'Logging into Docker Hub...'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Pushing image to Docker Hub...'
                sh """
                docker push ${DOCKER_USER}/${IMAGE_NAME}:${IMAGE_TAG}
                docker push ${DOCKER_USER}/${IMAGE_NAME}:latest
                """
            }
        }

        stage('Deploy Web Container') {
            steps {
                echo 'Deploying web application container...'
                sh """
                docker rm -f ${CONTAINER_NAME} || true
                docker run -d -p 5000:5000 --name ${CONTAINER_NAME} \
                ${DOCKER_USER}/${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        success {
            echo '✅ Docker CI/CD Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
        always {
            echo '🔁 Pipeline execution finished.'
        }
    }
}
