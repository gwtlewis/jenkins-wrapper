#!/usr/bin/env bash

start(){
        python ./scripts/bootstrap.py "./vars/main.yml"
        echo "Starting Jenkins"
}

stop(){
        echo "TODO"
}

status(){
        echo "TODO"
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
                echo "\n"
                echo "Usage: ./control.sh {start/stop/status}"
                exit 1
        ;;
esac
