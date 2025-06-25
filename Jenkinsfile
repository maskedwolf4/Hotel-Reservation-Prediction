pipeline{
    agent any

    stages{
        stage('Cloning from GitHub Repo'){
            steps{
                script{
                    echo 'Cloning from Github repo'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/maskedwolf4/Hotel-Reservation-Prediction']])
                }
            }
        }
    }
}