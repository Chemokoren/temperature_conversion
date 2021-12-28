pipeline{
    agent any
    stages{
        stage("Build"){
            steps{
                sh 'pip install -r requirements.txt'
            }
        }
        stage("Test"){
            steps{
                sh 'python manage.py test temperature'
            }
        }
        stage("Deploy"){
            steps{
                echo 'Deploying'
            }
        }
    }

    

}