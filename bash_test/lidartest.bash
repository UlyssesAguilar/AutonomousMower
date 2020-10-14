#!/bin/bash

gnome-terminal -- roscore
sleep 2s

#Start the LIDAR node in the seperate ubuntu terminal
echo "Start the LIDAR node"
echo ""
gnome-terminal -- roslaunch rplidar_ros rplidar_s1.launch

#Start the Safety node in the seperate ubuntu terminal
echo "Start the Safety node"
echo ""
gnome-terminal -- roslaunch safety check_distance_launch.launch

#Print Output
echo "Start the Safety node"
echo ""
gnome-terminal -- rostopic echo stop_vehicle
