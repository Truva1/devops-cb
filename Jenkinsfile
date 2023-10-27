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

        stage('Análisis de seguridad') {
            steps {
                dependencyCheck additionalArguments: '''
                    --failOnCVSS 7
                    -o './'
                    -s './'
                    -f 'ALL' 
                    --prettyPrint''', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
                    //falla si encuentra una vulnerailidad con puntaje superior a 7
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Ejecutar analisis sonarCloud') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    bat '''
                        sonar-scanner.bat \
                            -D"sonar.organization=truva1" \
                            -D"sonar.projectKey=Truva1_devops-cb" \
                            -D"sonar.sources=." \
                            -D"sonar.host.url=https://sonarcloud.io"
                    '''
                }
            }
        } 

        stage('Construir y subir imagen de Docker') {
            steps {
                bat 'docker build -t julian014/app-python-cb:latest .'
                withCredentials([usernamePassword(credentialsId: 'dockHub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat 'docker login -u %USERNAME% -p %PASSWORD%'
                    bat 'docker push julian014/app-python-cb:latest'
                }
            }
        }

    }
}
