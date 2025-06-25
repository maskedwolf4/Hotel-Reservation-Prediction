pipeline{
    agent any

    environment{
        VENV_DIR = 'venv'
    }

    stages{
        stage('Cloning from GitHub Repo'){
            steps{
                script{
                    echo 'Cloning from Github repo'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/maskedwolf4/Hotel-Reservation-Prediction']])
                }
            }
        }

        stage('Setting up Virtual ENV for Jenkins'){
            steps{
                script{
                    echo 'Setting up Virtual ENV for Jenkins'
                    sh '''
                    python venv -m ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .                   
                    '''
                }
            }
        }
    }
}