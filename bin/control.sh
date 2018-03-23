#!/usr/bin/env bash

start(){
        nohup java -jar jenkins.war --httpPort=8001 > jenkins-nohup.log 2>&1 & echo $! > jenkins.pid
        echo "Starting Jenkins"
}

stop(){
        if ps -p $(cat jenkins.pid) > /dev/null
        then
                kill jenkins.pid
                echo "Jenkins stopped"
        fi
}

status(){
        if ps -p $(cat jenkins.pid) > /dev/null
        then
                echo "Jenkins running"
        fi
}

case $1 in
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
                exit 1
        ;;
esac
