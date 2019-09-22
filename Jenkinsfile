node("MASTER"){
    stage('Clone Repo')
    {
        sh'''
            python stage_1.py
        '''

    }

     post {
        always {
            cleanWs()
            sh 'docker system prune -a -f --filter "label!=build-agent"'
        }
    }

}