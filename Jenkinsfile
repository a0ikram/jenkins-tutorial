pipeline("MASTER") {

       agent {
                docker {
                            image 'image-build-agent'
                            args dockerArgs('--network="host"')
                            label 'MASTER'
                            }
   }

    stages{
    stage('Clone Repo')
    {
        sh'''
            python3 stage_1.py
        '''

    }
    }

     post {
        always {
            cleanWs()
            sh 'docker system prune -a -f --filter "label!=build-agent"'
        }
    }

}