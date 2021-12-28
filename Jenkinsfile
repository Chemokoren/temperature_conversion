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
                sh 'ssh kibsoft@192.168.0.105 "source temp_env/bin/activate;\
                cd temperature_converter;\
                git pull origin master;\
                git config pull.ff only\
                pip install -r requirements.txt --no-warn-script-location;\
                python manage.py migrate;\
                deactivate;\
                sudo systemctl restart nginx;\
                sudo systemctl restart gunicorn "'
            }
        }
    }

    

}
// -o StrictHostKeyChecking=no 