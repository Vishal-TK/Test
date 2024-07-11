pipeline {

    agent any
 
    stages {

        stage('SCA') {

            steps {

                 script {

                    try {

                        bat 'D:/Snyk/snyk-win.exe code test D:/Snyk/DVWA-master >> D:/Snyk/Report1.txt'

                    } catch (Exception e) {

                        echo "Snyk test failed, but build continues"

                    }

                 }

            }

        }

    }

}
 