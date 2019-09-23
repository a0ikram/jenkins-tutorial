node("MASTER"){
    stage('Clone Repo')
    {
        sh'''
            rm -rf jenkins-tutorial
            rm -rf catfish_env
            rm package_v1.0.tar.gz
            git clone https://github.com/a0ikram/jenkins-tutorial.git/
        '''

    }
    stage("create virtual env")
    {
            echo ("creating virtual environment tutorial_env")
            sh '/Users/Shared/Jenkins/Library/Python/3.7/bin/virtualenv tutorial_env'
            echo ("running tutorial_env")
            sh 'source tutorial_env/bin/activate'
    }
    stage('running app')
    {
        sh'''
            cd jenkins-tutorial
            /usr/local/bin/pip3 install -r requirements.txt --user
            /usr/local/bin/python3 main.py
        '''

    }
    stage('package')
    {
        sh 'cd ..'
        sh 'tar -zcvf package_v1.0.tar.gz jenkins-tutorial'
        sh 'ls'

    }
        stage('cleaning space')
    {
        sh'''
            rm -rf jenkins-tutorial
            rm -rf catfish_env
            rm package_v1.0.tar.gz
        '''

    }

}