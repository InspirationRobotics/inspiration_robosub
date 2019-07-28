#! /bin/bash

function finish() {
    echo "killed"
    exit
}

trap finish SIGINT

while true
do
    if [[ $(cat /sys/class/gpio/gpio20/value) == 1 ]]
    then	
	
	pkill python
	./motors_kill
        echo "killed"
	
    fi
    sleep 0.050
    
done    
