pipeline {
    agent any
    stages {
        stage('Clonar Código') {
            steps {
                checkout scm
            }
        }
        stage('Ejecutar Pruebas Python') {
            steps {
                sh '''
                    docker create --name pruebas-${BUILD_NUMBER} -w /app python:3.11-slim python -m unittest test_app.py
                    docker cp . pruebas-${BUILD_NUMBER}:/app
                    docker start -a pruebas-${BUILD_NUMBER}
                '''
            }
            post {
                always {
                    sh 'docker rm -f pruebas-${BUILD_NUMBER} || true'
                }
            }
        }
    }
}
