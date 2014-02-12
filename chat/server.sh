#!/bin/bash

if [ $1 == "start" ]; then
	echo "Starting server ..."
	python websocket_server.py > ws.log 2>&1 &
elif [ $1 == "stop" ]; then
	echo "Stopping server ..."
	process=$(ps aux | grep 'python websocket_server.py' | grep -v 'grep' | awk '{split($0,a," "); print a[2]}')
	if [ "$process" == "" ]; then
		echo "No server running ..."
	else
		echo "Killing process with id $process ..."
		kill -9 $process
	fi
fi
