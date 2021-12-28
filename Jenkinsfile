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
                sh 'ssh kibsoft@192.168.0.105 "\
                virtualenv -p python3 myenv;\
                source myenv/bin/activate;\
                git clone git@github.com:Chemokoren/temperature_conversion.git;\
                git pull origin main;\
                cd temperature_conversion;\
                pip install -r requirements.txt --no-warn-script-location;\
                python manage.py migrate;\
                deactivate "'
            }
        }
    }

    

}
// -o StrictHostKeyChecking=no 
// sudo systemctl restart nginx;\
// sudo systemctl restart gunicorn
// git config pull.ff only\
// source temp_env/bin/activate;\