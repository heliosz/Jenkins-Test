pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out repository...'
                checkout scm
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m unittest test_app.py -v'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}