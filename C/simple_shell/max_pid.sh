#!/bin/bash

# Check if /proc/sys/kernel/pid_max exists
if [ -e /proc/sys/kernel/pid_max ]; then
    max_pid=$(cat /proc/sys/kernel/pid_max)
    echo "Maximum PID value: $max_pid"
else
    echo "Unable to determine maximum PID value."
fi
