import os

os.system("wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -")
os.system("echo 'deb https://download.sublimetext.com/ apt/stable/' | sudo tee /etc/apt/sources.list.d/sublime-text.list")
os.system("sudo apt-get update")
os.system("sudo apt-get install sublime-text")