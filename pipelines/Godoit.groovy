//scripted pipeline

def checkoutCode(String repoName, String branch){
    def repoUrl = "git@github.com:gwtlewis/${repoName}.git"
    sh "rm -rf *"
    sh "git clone ${repoUrl}"
    sh "cd ${WORKSPACE}/${repoName}; git checkout ${branch}"
    echo "${WORKSPACE}"
}

node{
    def repoName = 'godoit'
    def branch = 'master'

    stage("Checkout code from Git"){
        checkoutCode(repoName, branch)
    }

    stage("Retrieve dependency"){
        sh "go version"
        sh "go get -u github.com/natefinch/lumberjack"
        sh "go get github.com/influxdata/config"
        sh "go get -u github.com/robfig/cro"
    }

    withEnv(["GOPATH=${WORKSPACE}/${repoName}"]){

        stage("Test"){
            sh "echo ${GOPATH}"
        }

        stage("Build"){
            sh "echo ${GOPATH}"
        }
    }

    post {
        always {
            echo "always run"
        }
        failure{
            echo "run when fail"
        }
    }

}

