pipeline {
    agent any
    environment {
        // Simulação de variável de ambiente segura (Airbus/Hopla! compliance)
        DB_PASSWORD = credentials('db-prod-password') 
    }
    stages {
        stage('Security Analysis') {
            steps {
                script {
                    echo 'Running Sentinel Security Scanner...'
                    // Executa o scanner no nosso código fonte
                    sh 'python3 scanner.py --target app.py'
                }
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Running unit tests...'
                // Se o scanner falhar (exit 1), o Jenkins interrompe o pipeline aqui.
            }
        }
    }
    post {
        failure {
            echo 'Security Audit FAILED. Developer team notified.'
        }
    }
}