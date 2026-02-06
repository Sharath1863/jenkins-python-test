pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-python-app"
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

        stage('Create Artifact') {
            steps {
                echo 'Creating build artifact...'

                bat '''
                if exist build rmdir /s /q build
                mkdir build
                copy hello.py build\\
                copy requirements.txt build\\
                '''

                bat 'powershell Compress-Archive -Path build\\* -DestinationPath build\\app_build.zip'
            }
        }

        stage('Archive Artifact') {
            steps {
                echo 'Archiving artifact...'
                archiveArtifacts artifacts: 'build/app_build.zip', fingerprint: true
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t %IMAGE_NAME% .'
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
            echo 'CI/CD Docker Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
