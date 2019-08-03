#!/usr/bin/env python3

#this project was inspired by the hardish in BSSE students in installing laravel on linux/mac
#please do not run script as root for better functionality

#let us import the modules required for the script
import requests
from pathlib import Path
from urllib.request import urlretrieve
import os
import shutil

#split the logic into functions


def Xampp():
    #check if xampp install path exists
    
    dir = Path("/opt/lampp/")
    if not dir.exists():
        choice = str(input("Do you have xampp file on computer (YES,NO):"))
        if choice in ['yes','YES','y','Y']:
            print("Please move the file to the newly created folder xampp in %s and press Enter\n" %os.getcwd())
            
            input("PRESS ANY KEY WHEN COPY IS DONE:")
            os.system("mv *.run xampp.run")
       
        
        else:
                url = 'https://www.apachefriends.org/xampp-files/7.3.7/xampp-linux-x64-7.3.7-1-installer.run'
                dst = 'xampp.run'
                urlretrieve(url, dst)

    else:
        print("\n xampp install already existing. installing other requirements ..... \n \n")


    #instructions to execute after decision making 
    os.system("echo %s | sudo -S chmod +x xampp.run" %pwd)
    os.system("echo %s | sudo -S ./xampp.run" %pwd)
    os.system("echo %s | sudo -S ln -s /opt/lampp/bin/php /usr/local/bin/php" %pwd)
    os.system("echo %s | sudo -S /opt/lampp/xampp start" %pwd)


def composer():
    #this will check if composer exists and unistall it then re-install it
    print("\n performing actions on composer....")
    user = os.listdir("/home")
    user = user[0]
    x = "/home/"+ user
    x+="/.config/composer"
    w = "/home/"+ user + "/.composer"
    compUbuntu = Path(w)
    if compUbuntu.exists():
            print("\n removing composer folder \n")
            shutil.rmtree(w)

    compInstall = Path(x)
    if compInstall.exists():
        print("\n removing composer folder \n")
        shutil.rmtree(x)
    dir = "/home/"+ user
    os.chdir(dir)
    print(" \n installing composer")
    cinst = '''php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
                php -r "if (hash_file('sha384', 'composer-setup.php') === '48e3236262b34d30969dca3c37281b3b4bbe3221bda826ac6a9a62d6444cdb0dcd0615698a5cbe587c3f0fe57a54d8f5') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
                php composer-setup.php
                php -r "unlink('composer-setup.php');
             "'''
    os.system(cinst)
    os.system("echo %s | sudo -S mv composer.phar /usr/local/bin/composer" %pwd)
    print("\033[31m ...........CREATING LARAVEL PROJECT.... PLEASE WAIT \033[31m") 
    os.system("composer create-project --prefer-dist laravel/laravel %s" %name)
    os.chdir("%s" %name)
    os.system("php artisan serve")

def banner():
    logo = ''' \033[32m
        **************************************************************** 
                ***    ****    *****   *****         *****
                ***    ****    *****     *****      *****
                ***    ****    *****       *****   *****
                ***********    *****         **** ****  
                ***    ****    *****        *****  *****
                ***    ****    *****       *****     *****
                ***    ****    *****     *****        *****
        **************************************************************** 
                A LARAVEL INSTALLER BY KALI HIX 
                        dalirichardh@gmail.com
                        PROGRAMMERS OVER MORTAL-MEN
         \033[32m'''
    print(logo)

def env():
    #adding xampp php to local environment
    #just editing the /etc/environment file
    print("moving php to local path...... ")
    os.system("echo %s | sudo -S ln -s /opt/lampp/bin/php /usr/local/bin/php")
    instpath = 'PATH=("/opt/lampp/bin/php:'
    os.system("echo | cat /etc/environment > environment.txt")
    with open("environment.txt","r+") as lpath:
        x =''
        for line in lpath:
                x = line.split('"')[1]
                x = instpath + x
                x+= '")'
        lpath.seek(0)
        lpath.truncate(0)
        lpath.write(x)
        lpath.close()
    os.system("echo %s | sudo -S mv environment.txt /etc/environment")
    print("done")

        
#let us fire up this shit......

if __name__ == '__main__':
        banner()
        if os.geteuid() != 0:
                
                name = str(input("\033[32m PLEASE ENTER THE NAME OF THE PROJECT: \n \033[32m"))
                pwd  = str(input("\n PLEASE ENTER PC PASSWORD:"))

                Xampp()
                env()
                composer()

        else:
                print(" \033[31m PLEASE DON'T RUN SCRIPT AS ROOT \033[31m")


os.remove()


    
