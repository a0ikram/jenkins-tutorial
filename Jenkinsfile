node("MASTER"){
    stage('Clone Repo')
    {
        sh'''
            rm -rf jenkins-tutorial
            git clone https://github.com/a0ikram/jenkins-tutorial.git/
        '''

    }
    stage('running app')
    {
        sh'''
        set +x
            dt=$(date '+%d/%m/%Y %H:%M:%S');
            echo "$dt"
            cd jenkins-tutorial
            python selenium_example.py
        '''

    }
        stage('cleaning space')
    {
        sh'''
            rm -rf jenkins-tutorial
        '''

    }

}