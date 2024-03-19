def getTag(fileName) {
    return sh(
                script: "grep -e \"tag:\" $fileName | awk \'{ print \$2 }\' | tr -d \'\"\'",
                returnStdout: true
            ).trim()
}

pipeline {
    agent {
         label "data-engineering"
    }
    environment {
        REGISTRY="${AWS_TOOLING_ACCOUNT}.dkr.ecr.eu-west-1.amazonaws.com"
        IMAGE_NAME = "${REGISTRY}/data/superset"
        AWS_DEFAULT_REGION = "eu-west-1"
    }
    options {
        skipStagesAfterUnstable()
        disableConcurrentBuilds()
        parallelsAlwaysFailFast()
        timestamps()
    }
    stages {
        stage("Get image tag") {
            steps {
                script {
                    IMAGE_TAG = getTag("config.yaml")
                }
            }
        }
        stage("Build") {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }
        stage("Push") {
            steps {
                sh "aws ecr get-login-password | docker login --username AWS --password-stdin $REGISTRY"
                sh "aws ecr describe-repositories --repository-names data/superset ||  aws ecr create-repository --repository-name data/superset --image-scanning-configuration scanOnPush=true"
                sh "docker push $IMAGE_NAME:$IMAGE_TAG"
            }
        }
    }
    post {
        always {
            script {
                echo "Stopping containers"
                def docker_containers = sh(script: 'docker ps -q', returnStdout: true).split()
                for (container in docker_containers) {
                    sh "docker stop ${container} || true"
                }
                echo "Deleting images"
                def docker_images = sh(script: 'docker ps -aq', returnStdout: true).split()
                for (image in docker_images) {
                    sh "docker rm ${image} || true"
                }
            }
        }
    }
}
