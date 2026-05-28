pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/API_Automation_Framework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -v --alluredir=reports'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'reports']]
                ])
            }
        }
    }
}