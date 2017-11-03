pipeline {
  agent none
  stages {
    stage('stage 1') {
      parallel {
        stage('stage 1') {
          steps {
            echo 'hello world'
          }
        }
        stage('stage 2') {
          steps {
            sleep 5
          }
        }
      }
    }
    stage('stage 3') {
      steps {
        sh 'printenv'
      }
    }
  }
}