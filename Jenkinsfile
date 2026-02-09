pipeline {
agent any

environment {
    IMAGE_NAME = "sharath2003/my-python-app"
    IMAGE_TAG = "${BUILD_NUMBER}"
    CONTAINER_NAME = "my-python-container"
}

stages {

    stage('Build Docker Image') {
        steps {
            sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
        }
    }

    stage('Docker Login') {
        steps {
            withCredentials([usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )]) {
                sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
            }
        }
    }

    stage('Push Image') {
        steps {
            sh "docker push $IMAGE_NAME:$IMAGE_TAG"
        }
    }

    stage('Deploy New Version') {
        steps {
            sh """
            docker stop $CONTAINER_NAME || true
            docker rm $CONTAINER_NAME || true
            docker run -d -p 5000:5000 \
            --name $CONTAINER_NAME \
            $IMAGE_NAME:$IMAGE_TAG
            """
        }
    }

    stage('Health Check') {
        steps {
            script {
                sleep 10
                def status = sh(
                    script: "curl -s -o /dev/null -w '%{http_code}' http://localhost:5000/health",
                    returnStdout: true
                ).trim()

                if (status != "200") {
                    error "Health check failed!"
                }
            }
        }
    }
}

post {
    failure {
        script {
            echo "Deployment failed — rolling back..."

            def previousTag = IMAGE_TAG.toInteger() - 1

            sh """
            docker stop $CONTAINER_NAME || true
            docker rm $CONTAINER_NAME || true
            docker run -d -p 5000:5000 \
            --name $CONTAINER_NAME \
            $IMAGE_NAME:$previousTag
            """
        }
    }
}