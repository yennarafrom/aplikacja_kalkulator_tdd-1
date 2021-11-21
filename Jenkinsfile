pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    sh 'echo Checkout branch $BRANCH ...'
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'git branch: \'main\', url: \'https://github.com/yennarafrom/aplikacja_kalkulator_tdd-1.git\'']]])
                }
            }
        } // END OF STAGE Chackout
        stage('MAIN TEST') {
            steps {
                script {
                    sh 'echo Testing ...'
                    sh 'pytest --html=report.html'
                }
            }
        } // END OF STAGE MAIN TEST
        
    } // END OF STAGES
} // END OF PIPELINE
