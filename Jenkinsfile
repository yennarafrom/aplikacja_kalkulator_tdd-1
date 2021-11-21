pipeline {
    agent any
    parameters {
    gitParameter branchFilter: '.*', defaultValue: 'main', name: 'BRANCH', type: 'PT_BRANCH'
    }

    stages {
    stage('Example') {
      steps {
        git branch: "${params.BRANCH}", url: 'https://github.com/yennarafrom/aplikacja_kalkulator_tdd-1.git'
      }
    }   
        stage('Checkout') {
            steps {
                script {
                    sh 'echo Checkout branch $BRANCH ...'
                    checkout([$class: 'GitSCM', branches: [[name: '.*']], extensions: [], userRemoteConfigs: [[url: 'git branch: \'main\', url: \'https://github.com/yennarafrom/aplikacja_kalkulator_tdd-1.git\'']]])
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
