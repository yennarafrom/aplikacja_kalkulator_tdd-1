pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    sh 'echo Checkout ...'
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/yennarafrom/aplikacja_kalkulator_tdd-1.git']]])
                }
            }
        } // END OF STAGE BUILD
    } // END OF STAGES
} // END OF PIPELINE
