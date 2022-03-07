#!/bin/bash

export $(xargs <.env)

if [ -f $PATH_PID/server.pid ] && [ $(cat $PATH_PID/server.pid | wc -w) -gt 0 ]; then
	echo "[ERROR] SERVER is still running at pid $(cat $PATH_PID/server.pid)!"
	echo "[ERROR] Please run ./kill_server.sh to shut it down"
	exit 1
fi
nohup python3 manage.py runserver > $PATH_LOG/nohup_server.log &
server_pid=$(echo $!)
echo $server_pid > $PATH_PID/server.pid
echo "Started Django Server - Log in $PATH_LOG/server.log - PID $server_pid"
