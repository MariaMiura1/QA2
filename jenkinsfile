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
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                // Ejecutamos pytest y generamos un reporte JUnit para Jenkins
                sh 'pytest -v --junitxml=test-results/pytest-results.xml'
            }
        }
    }

    post {
        always {
            // Publicar resultados de tests en Jenkins
            junit 'test-results/pytest-results.xml'
        }
    }
}
