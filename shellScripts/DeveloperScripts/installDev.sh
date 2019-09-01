#!/bin/bash

# git
sudo apt install -y git

# common
sudo apt install build-essentials

# vs code
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update -y
sudo apt install -y code
sudo rm -f microsoft.gpg

# python 3
sudo add-apt-repository ppa:deadsnakes/ppa -y )
sudo apt install -y python3

# golang
wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.12.7.linux-amd64.tar.gz
sudo rm -f go1.12.7.linux-amd64.tar.gz
echo "export PATH=$PATH:/usr/local/go/bin"

# java
sudo apt install -y default-jre
sudo apt install -y default-jdk
sudo apt-get install maven -y

# node
curl -sL https://deb.nodesource.com/setup_12.x | sudo bash - #Submit the version according to your need.
sudo apt install -y nodejs

# Docker
curl -fsSL get.docker.com -o get-docker.sh
sh get-docker.sh
# Docker-compose
sudo pip install docker-compose
