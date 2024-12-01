pipeline {
  agent { label 'JenkinsAgent' }
  tools {
    jdk 'Java17'
    maven 'Maven3'
  }
  stages{
    stage("Cleanup Workspace"){
      steps { 
        cleanWs()
      }
  }
    stage("Checkout from SCM"){
      steps {
        git branch: 'main', credentialsID: 'github', url: 'https://github.com/gbhasin0828/python-ci-cd-demo'
      }
    stage("Build Application"){
      steps{
        sh "mvn clean package"
      }
    }

      stage("Test Application"){
        steps{
          sh "mvn test"
        }
      }
    }
  }
}
