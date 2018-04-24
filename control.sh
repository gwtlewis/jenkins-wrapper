#!/usr/bin/env bash

deploy(){
        start

        PID=$(cat ./logs/jenkins.pid)
        echo "First starting Jenkins, PID - ${PID}"

        while true
        do
            grep "Jenkins is fully up and running" jenkins-nohup.log
            if [ $? == 0 ]; then
                nohup python ./scripts/configure.py "./vars/main.yml" ${PID} > jenkins-nohup.log 2>&1
                break
            fi
            sleep 1
        done

        start
}

start(){
        nohup python ./scripts/bootstrap.py "./vars/main.yml" > jenkins-nohup.log 2>&1
        echo "starting Jenkins"
}

stop(){
        kill $(cat ./logs/jenkins.pid)
        echo "Jenkins stopped"
}

status(){
        if ps -p $(cat ./logs/jenkins.pid) > /dev/null ; then
            echo "Jenkins running"
        else
            echo "Jenkins down"
        fi
}

case $1 in
        'deploy')
                deploy
        ;;
        'start')
                start
        ;;
        'stop')
                stop
        ;;
        'status')
                status
        ;;
        * )
                echo "Invalid action."
                echo "\n"
                echo "Usage: ./control.sh {deploy/start/stop/status}"
                exit 1
        ;;
esac
