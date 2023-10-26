pipeline {
    agent any 

    stages {
        stage('Clonar repositorio') {
            steps {
                checkout scm 
            }
        }
        
        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh 'pytest'
            }
        }

        stage('Construir y subir imagen de Docker') {
            steps {
                sh 'docker build -t app-python-cb:latest .'
                // Sube la imagen a Docker Hub
                withCredentials([usernamePassword(credentialsId: 'dockHub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'docker login -u $USERNAME -p $PASSWORD'
                    sh 'docker push app-python-cb:latest .'
                }
            }
        }
    }
}
