#!/bin/bash

gnome-terminal -- roscore
sleep 2s

#Start the GPS node in the seperate ubuntu terminal
echo "Start GPS node"
echo ""
gnome-terminal -- roslaunch ublox_gps ublox_zed-f9p.launch

sleep 2s
#Start the waypoint following node in the seperate ubuntu terminal
echo "Start the waypoint following node"
echo ""
gnome-terminal -- roslaunch waypoint_following waypoint_following_launch.launch
