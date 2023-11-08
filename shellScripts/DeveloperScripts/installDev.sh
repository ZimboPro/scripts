#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# git
sudo apt install -y git

#Setting up Git
read -p "${c}Do you want to setup Git global config? (y/n): " -r; $r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
	echo -e "${c}Setting up Git"; $r
	(set -x; git --version )
	echo -e "${c}Setting up global git config at ~/.gitconfig"; $r
	git config --global color.ui true
	read -p "Enter Your Full Name: " name
	read -p "Enter Your Email: " email
	git config --global user.name "$name"
	git config --global user.email "$email"
	echo -e "${c}Git Setup Successfully!"; $r
else
	echo -e "${c}Skipping!"; $r && :
fi

# common
sudo apt install -y build-essentials file

# vs code
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt-get install -y apt-transport-https
sudo apt update -y
sudo apt install -y code
sudo rm -f microsoft.gpg

# python 3
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt-get update -y
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

# C
sudo apt install -y build-essentials clang gcc gdb glibc

# c++
sudo apt install -y clang++ g++

# homebrew
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"

# valgrind and cmake
brew install cmake
brew install valgrind

# rust
curl -sf -L https://static.rust-lang.org/rustup.sh | sh
