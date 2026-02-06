pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Run Python Script') {
            steps {
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
                archiveArtifacts artifacts: 'build/app_build.zip', fingerprint: true
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying application from artifact...'

                bat '''
                if exist deploy rmdir /s /q deploy
                mkdir deploy
                '''

                bat 'powershell Expand-Archive -Path build\\app_build.zip -DestinationPath deploy'

                bat '''
                cd deploy
                pip install -r requirements.txt
                python hello.py
                '''
            }
        }

    }

    post {
        success {
            echo 'CI/CD Pipeline executed successfully!'
        }
    }
}
