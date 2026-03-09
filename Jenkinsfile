pipeline {

    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-api .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 aceest-api'
            }
        }

    }
}
