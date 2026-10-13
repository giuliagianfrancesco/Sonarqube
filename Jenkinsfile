pipeline {
  agent any
  stages {
    stage('SonarQube analysis') {
      steps {
        script {
          scannerHome = tool 'sonar-scanner'
        }
        withSonarQubeEnv('sonarqube-lab') {
          sh "${scannerHome}/bin/sonar-scanner -Dsonar.verbose=true"
        }
      }
    }
    stage('Quality Gate') {
      steps {
        timeout(time: 5, unit: 'MINUTES') {
          waitForQualityGate abortPipeline: true
        }
      }
    }
  }
}
