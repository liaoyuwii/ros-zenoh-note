FROM osrf/ros:humble-desktop

RUN apt update && apt upgrade -y

RUN apt install -y python3-pip curl vim

RUN pip3 install eclipse-zenoh

RUN apt install -y ros-humble-zenoh-bridge-dds
