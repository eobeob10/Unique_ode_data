#!/bin/bash

sudo apt-get update



#Installing FTPd service
sudo apt-get install -y vsftpd


#Allowing anonymous access via FTP
sudo cp /data/new_vsftpd.conf /etc/vsftpd.conf
sudo systemctl restart vsftpd

#Allowing ssh private key login
sudo cp /data/our_sshd_config /etc/sshd_config
sudo systemctl restart sshd


# Create a directory containing the credentials file for anonymous FTP to read
sudo mkdir -p /var/ftp/pub
sudo chown nobody:nogroup /var/ftp/pub
sudo mkdir /var/ftp/pub/.data/
sudo echo "Irregular_Odes_suck! (and so does this flag)" > /var/ftp/pub/flag.txt
sudo cp /data/creds /var/ftp/pub/.data/hmmm

# Creating the Pindaric user
sudo deluser Pindaric
sudo delgroup Pindaric
sudo useradd Pindaric
sudo mkdir -p /home/Pindaric
sudo chown Pindaric:Pindaric /home/Pindaric
sudo usermod -s /bin/bash Pindaric
sudo bash -c "echo 'Pindaric:Stesich0ru5_R0cK5' | chpasswd"


#Add the bytecode for cmd service to the Pindaric's home
sudo cp /data/login.pyc Pindaric:Pindaric /home/Pindaric/login.pyc
sudo chown Pindaric:Pindaric /home/Pindaric/login.pyc

# Creating the Horatian user
sudo deluser Horatian
sudo delgroup Horatian
sudo useradd Horatian
sudo mkdir -p /home/Horatian
sudo chown Horatian:Horatian /home/Horatian
sudo usermod -s /bin/bash Horatian
sudo bash -c "echo 'Horatian:1_1Iv3_f0r_H0rAc3_95995' | chpasswd"

#Deleting the Ubuntu user
sudo deluser ubuntu
sudo delgroup ubuntu
sudo rm -rf /home/ubuntu

#Deleting the Vagrant user
sudo deluser vagrant
sudo delgroup vagrant
sudo rm -rf /home/vagrant

#Installing pip to get pycrypto
sudo apt-get install -y python3-pip
sudo pip3 install pycrypto 
sudo pip3 install pyinstaller

#Moving the service to a directory
sudo mkdir -p /var/cmd/
sudo cp /data/login.py /var/cmd/.cmd_service.py
sudo chmod +x /var/cmd/.cmd_service.py

# Making the login function as a service
sudo cp /data/service /etc/systemd/system/cmd.service
sudo systemctl daemon-reload
sudo systemctl enable cmd.service
sudo systemctl restart cmd.service

# Creating the Horatian flag
sudo bash -c 'echo "c2667c3c95fccd6d26bca154dd0be048" > /home/Horatian/user.txt'
sudo chown -R Horatian:Horatian /home/Horatian/user.txt
sudo chmod 600 /home/Horatian/user.txt

sudo cp /data/unique_ode/ /home/Horatian/unique_ode/
sudo chmod 600 /home/Horatian/unique_ode/unique_ode


# Creating the root flag
sudo bash -c 'echo "9525ad90456e7765bf8f112326fca9b2" > /root/$(printf "\u2000root.txt")'



# Enabling ssh login to Horatian via private key
sudo mkdir -p /home/Horatian/.ssh
sudo cp /data/Horatian_id_rsa /home/Horatian/.ssh/Horatian_id_rsa
sudo chmod 644 /data/Horatian_id_rsa /home/Horatian/.ssh/Horatian_id_rsa
sudo cp /data/Horatian_id_rsa.pub /home/Horatian/.ssh/Horatian_id_rsa.pub
sudo cp /data/Horatian_id_rsa.pub /home/Horatian/.ssh/authorized_keys
sudo chown -R Horatian:Horatian /home/Horatian


# Getting the unique_ode binary to Horatian's home directory
sudo cp /data/unique_ode.py /home/Horatian/
sudo pyinstaller /home/Horatian/unique_ode.py --distpath /home/Horatian/
sudo chown -R Horatian:Horatian /home/Horatian
sudo chmod 100 /home/Horatian/unique_ode/unique_ode
sudo rm /home/Horatian/unique_ode.*
sudo rm -r /home/Horatian/__pycache__/
sudo rm -r /home/Horatian/build/

#updating sudoers file for setuid
sudo cp /data/our_sudoers /etc/sudoers


#allow FTP, ssh and python service connectivity
sudo ufw default deny outgoing
sudo ufw default deny incoming
sudo ufw allow 20/tcp
sudo ufw allow 20/udp
sudo ufw allow 21/udp
sudo ufw allow 21/tcp
sudo ufw allow 22/tcp
sudo ufw allow 64000:64321 proto tcp
sudo ufw allow 64000:64321 proto udp
sudo ufw --force enable
sudo ufw reload

sudo iptables -t raw -A PREROUTING -p tcp -m tcp --dport 21 -j CT --helper ftp

#Removing the data folder
sudo umount /data
