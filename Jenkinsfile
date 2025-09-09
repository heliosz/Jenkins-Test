@Library('pipeline-library@0.5.5') _

import com.creatio.jenkins.PipelineEnvironment

Map config = readYaml(text: """
general:
  projectName: 'jenkins-test'
  publishPipelineState: false
  useExtendedVersioning: false
  buildTool: python
kubernetes:
  containers:
  - containerName: python
    image: python:${PYTHON_VERSION}
""")

pipelineWrap(config) {
    stage('Run Unit Tests') {
        container('python') {
            sh 'python3 -m unittest test_app.py -v'
        }
    }
}