pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the local Git repository
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/master']], 
                          userRemoteConfigs: [[url: '/Users/yahayaohinoyi/Documents/CODING-PROJECTS/test']]])
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies using pip
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest
                sh 'pytest'
            }
        }

        // Add more stages for additional tasks (e.g., building, deploying, etc.) if needed
    }

    post {
        always {
            // Clean up the workspace (optional)
            deleteDir()
        }
    }
}
