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

    }

    post {
        success {
            echo 'Artifact created and archived successfully!'
        }
    }
}
