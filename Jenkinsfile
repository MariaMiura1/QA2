pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                // Usa python3 en lugar de python
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                // Ejecutar pytest con python3
                sh 'python3 -m pytest -v --junitxml=test-results/pytest-results.xml'
            }
        }
    }

    post {
        always {
            // Publicar resultados de tests (si existen)
            junit 'test-results/pytest-results.xml'
        }
    }
}
