#!/bin/bash
export $(xargs <.env)

server_pid=$(cat $PATH_PID/server.pid)
echo "SERVER PID: $server_pid"
ps -o pid= --ppid $server_pid
kill -9 $(ps -o pid= --ppid $server_pid)
kill -9 $server_pid
rm $PATH_PID/server.pid

echo "Kill server successfully!"
