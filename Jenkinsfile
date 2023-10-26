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
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                bat 'pytest'
            }
        }

        stage('Construir y subir imagen de Docker') {
            steps {
                bat 'docker build -t app-python-cb:latest .'
                // Sube la imagen a Docker Hub
                withCredentials([usernamePassword(credentialsId: 'dockHub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat 'docker login -u $USERNAME -p $PASSWORD'
                    bat 'docker push app-python-cb:latest .'
                }
            }
        }
    }
}
