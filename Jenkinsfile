pipeline {
agent any

```
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
                sh """
                echo $DOCKER_PASS | docker login \
                -u $DOCKER_USER --password-stdin
                """
            }
        }
    }

    stage('Push Image') {
        steps {
            sh "docker push $IMAGE_NAME:$IMAGE_TAG"
        }
    }

    stage('Stop Old Container') {
        steps {
            sh """
            docker stop $CONTAINER_NAME || true
            docker rm $CONTAINER_NAME || true
            """
        }
    }

    stage('Run New Container') {
        steps {
            sh """
            docker run -d -p 5000:5000 \
            --name $CONTAINER_NAME \
            $IMAGE_NAME:$IMAGE_TAG
            """
        }
    }
}
```

}
