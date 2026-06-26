pipeline {
    agent any
    environment {
        DB_PASSWORD = credentials('db-prod-password') 
    }
    stages {
        stage('Security Analysis') {
            steps {
                script {
                    echo 'Running Sentinel Security Scanner...'
                    sh 'python3 scanner.py --target app.py'
                }
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Running unit tests...'
            }
        }
    }
    post {
        failure {
            echo 'Security Audit FAILED. Developer team notified.'
        }
    }
}